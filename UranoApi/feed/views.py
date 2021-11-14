from django.shortcuts import render
from .models import Publication, PublicationW, PublicationI, Comments, CommentsW
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .forms import PublicationForm, PublicationWForm, PublicationIForm, CommentsForm, CommentsWForm
from taggit.models import Tag, slugify
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.urls import reverse, reverse_lazy
import pandas as pd
import folium
import geocoder
import re

from django.http import HttpResponseRedirect

def linkedtags(text):
    res = text.split()



    for words in res:



        if "@" in words or "#" in words:

                if len(words) > 1:

                    if words[0] == "@" and User.objects.filter(username=words[1:]):
                        l = words
                        text = text.replace(l, "<a href='/profile/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>")

                    elif words[0] == "@" and User.objects.filter(username=words[1:-1]):
                        l = words
                        m = l[-1]
                        l = l[:-1]
                        text = text.replace(l, "<a href='/profile/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>" + m)


                    elif words[0] == "#":


                        if words[-1] in (".", ",", "!", "?", ":", ";", ")", "}", "]", "'", '"'):
                            l = words
                            m = l[-1]
                            l = l[:-1]
                            text = text.replace(l, "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>"+ m)

                        else:
                            l = words
                            text = text.replace(l, "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>")


                    elif words[0] in  (".",",","¡","¿",":",";","(","{","[","'",'"'):


                	    if words[1] == "#":

                                if words[-1] in (".",",","!","?",":",";",")","}","]","'",'"'):
                                    l = words
                                    m = l[-1]
                                    s = l[0]
                                    l = l[1:-1]
                                    text = text.replace(l, s + "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>" + m)

                                else:
                                    l = words
                                    s = l[0]
                                    l = l[1:]
                                    text = text.replace(l, s + "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>" )


                    elif words[1] == "@" and User.objects.filter(username=words[2:]):
                        l = words
                        s = l[0]
                        l = l[1:]

                        text = text.replace(l, s + "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>" )

                    elif words[1] == "@" and User.objects.filter(username=words[2:-1]):
                        l = words
                        m = l[-1]
                        s = l[0]
                        l = l[1:-1]

                        text = text.replace(l, s + "<a href='/tags/" + l[1:] + "' style='color:#67E8F9'>" + l + "</a>"+ m)

                else:
                    pass

        else:
            pass

        text = re.sub("\n", "<br>",text)

    return(text)




def hastag(text):
    hashtag_list = []

    if text:

        for word in text.split():
            if word[0] == "#" and len(word) > 1:
                if word[-1] in (".",",","!","?",":",";",")","}","]","'",'"'):
                    hashtag_list.append(word[1:-1])

                else:
                    hashtag_list.append(word[1:])

            elif word[0] in (".",",","¡","¿",":",";","(","{","[","'",'"'):

                if word[1] == "#" and len(word) > 1:
                    if word[-1] in  (".",",","!","?",":",";",")","}","]","'",'"'):
                        hashtag_list.append(word[2:-1])

                    else:
                        hashtag_list.append(word[2:])

    return hashtag_list


def categorytag(text):
    category  = []
    res = text

    linked = ""

    for word in res:

        category.append(word)

        linked += '<a href="/tags/'+ word.lower() +'">' + word + ' </a>'

    return linked, category








class PublicationDetail(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'feed/publication_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comments.objects.filter(publication = context['publication']).order_by('datatime')

        context['comments'] = comments

        form = CommentsForm()

        context['form'] = form

        return context


    def post(self, request, pk, *args, **kwargs):

        publication = Publication.objects.get(pk=pk)
        form = CommentsForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            listtag = hastag(comment.text)
            comment.uname = request.user
            comment.publication = publication
            comment.tag_text = linkedtags(comment.text)


            comment.save()

            for tag in listtag:
                comment.tags.add(tag)



        form_n = CommentsForm()

        context= {}
        context['publication'] = publication
        context['form'] = form_n
        context['comments'] = Comments.objects.filter(publication = pk).order_by('datatime')

        return render(request, 'feed/publication_detail.html', context)



class AddLikeC(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comments.objects.get(pk=pk)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class AddDisLikeC(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        comment = Comments.objects.get(pk=pk)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comments
    template_name = 'feed/comment_confirm_delete.html'


    def post(self, request, post_pk, pk, *args, **kwargs):

        Comments.objects.filter(pk=pk).delete()

        return HttpResponseRedirect(reverse_lazy('publicationdetail', kwargs = {'pk': post_pk}))


    def test_func(self):
        publication = self.get_object()
        return self.request.user == publication.uname


class CommentEditView(UpdateView):
    model = Comments
    fields= ['text']
    template_name = 'feed/comment_edit.html'

    def form_valid(self, form):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.uname = self.request.user


        self.object.tags.clear()

        listtag = hastag(self.object.text)

        for tag in listtag:
            self.object.tags.add(tag)

        self.object = form.save()
        self.object.tag_text = linkedtags(self.object.text)
        self.object.save()

        return HttpResponseRedirect(reverse_lazy('publicationdetail', kwargs = {'pk': self.object.publication.pk}))


    def test_func(self):
        publication = self.get_object()
        return self.request.user == publication.uname


class PublicationWDetail(LoginRequiredMixin, DetailView):
    model = PublicationW
    template_name = 'feed/publicationw_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = CommentsW.objects.filter(publicationw = context['publicationw']).order_by('datatime')

        context['comments'] = comments

        form = CommentsWForm()

        context['form'] = form

        return context


    def post(self, request, pk, *args, **kwargs):

        publication = PublicationW.objects.get(pk=pk)
        form = CommentsWForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            listtag = hastag(comment.text)
            comment.uname = request.user
            comment.publicationw = publication
            comment.tag_text = linkedtags(comment.text)


            comment.save()

            for tag in listtag:
                comment.tags.add(tag)



        form_n = CommentsWForm()

        context= {}
        context['publicationw'] = publication
        context['form'] = form_n
        context['comments'] = CommentsW.objects.filter(publicationw = publication).order_by('datatime')

        return render(request, 'feed/publicationw_detail.html', context)


class AddLikeCW(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = CommentsW.objects.get(pk=pk)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class AddDisLikeCW(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        comment = CommentsW.objects.get(pk=pk)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class CommentWDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentsW
    template_name = 'feed/commentw_confirm_delete.html'


    def post(self, request, post_pk, pk, *args, **kwargs):

        CommentsW.objects.filter(pk=pk).delete()

        return HttpResponseRedirect(reverse_lazy('publicationwdetail', kwargs = {'pk': post_pk}))


    def test_func(self):
        publication = self.get_object()
        return self.request.user == publication.uname


class CommentWEditView(UpdateView):
    model = CommentsW
    fields= ['text']
    template_name = 'feed/commentw_edit.html'

    def form_valid(self, form):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.uname = self.request.user


        self.object.tags.clear()

        listtag = hastag(self.object.text)

        for tag in listtag:
            self.object.tags.add(tag)

        self.object = form.save()
        self.object.tag_text = linkedtags(self.object.text)
        self.object.save()

        return HttpResponseRedirect(reverse_lazy('publicationwdetail', kwargs = {'pk': self.object.publicationw.pk}))


    def test_func(self):
        publication = self.get_object()
        return self.request.user == publication.uname



class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/home.html'
    ordering = ['datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context['publicationt'] = Publication.objects.all().order_by('-datatime')
        context['publicationw'] = PublicationW.objects.all().order_by('-datatime')
        context['publicationi'] = PublicationI.objects.all().order_by('-datatime')

        return context


class PublicationTagsView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/tags.html'

    ordering = ['datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        warningmaps = []
        tag_name = self.kwargs.get('tag_slug')

        for publications in PublicationW.objects.filter(involved__slug=tag_name):
            WarningMaps = folium.Map(location=[publications.lat, publications.lon], zoom_start=10)

            toolmark = "ALERTA" + " " + str(str(slugify(publications.datatime))[:10] + " " + publications.case_id)

            folium.Marker([publications.lat, publications.lon], tooltip=toolmark,
                          popup=publications.description, icon=folium.Icon(color='yellow', icon='exclamation-triangle', prefix='fa')).add_to(WarningMaps)
            # Get HTML Representation of Map Object

            warningmaps.append(WarningMaps._repr_html_())



        TagsMaps = folium.Map(location=[4.583333, -74.066667], zoom_start=4, tiles="Stamen Terrain")

        publicationsw = PublicationW.objects.filter(involved__slug=self.kwargs.get('tag_slug')).order_by('-datatime')

        for publications in publicationsw:



            toolmark = "ALERTA" + " " + str(str(slugify(publications.datatime))[:10] + " " + publications.case_id)

            folium.Marker([publications.lat, publications.lon], tooltip=toolmark,
                          popup=publications.description, icon=folium.Icon(color='yellow', icon='exclamation-triangle', prefix='fa')).add_to(TagsMaps)
            # Get HTML Representation of Map Object

        tag_map = TagsMaps._repr_html_()

        context['publicationt'] = Publication.objects.filter(tags__slug=self.kwargs.get('tag_slug')).order_by('-datatime')
        context['publicationw'] = publicationsw
        context['publicationi'] = PublicationI.objects.all()
        context['tag_map'] = tag_map
        context['tag_name'] = tag_name

        return context


class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        publication = Publication.objects.get(pk=pk)

        is_dislike = False
        for dislike in publication.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            publication.dislikes.remove(request.user)

        is_like = False
        for like in publication.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            publication.likes.add(request.user)

        if is_like:
            publication.likes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class AddDisLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        publication = Publication.objects.get(pk=pk)

        is_like = False
        for like in publication.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            publication.likes.remove(request.user)

        is_dislike = False
        for dislike in publication.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            publication.dislikes.add(request.user)

        if is_dislike:
            publication.dislikes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class AddLikeW(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        publication = PublicationW.objects.get(pk=pk)

        is_dislike = False
        for dislike in publication.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            publication.dislikes.remove(request.user)

        is_like = False
        for like in publication.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            publication.likes.add(request.user)

        if is_like:
            publication.likes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class AddDisLikeW(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        publication = PublicationW.objects.get(pk=pk)

        is_like = False
        for like in publication.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            publication.likes.remove(request.user)

        is_dislike = False
        for dislike in publication.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            publication.dislikes.add(request.user)

        if is_dislike:
            publication.dislikes.remove(request.user)

        next = request.POST.get('next', '/')

        return HttpResponseRedirect(next)


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'feed/create.html'

    success_url = '/'
    form_class = PublicationForm

    def form_valid(self, form):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.uname = self.request.user

        self.object = form.save()
        self.listtag = hastag(self.object.text)

        for self.tag in self.listtag:
            self.object.tags.add(self.tag)



        self.object.tag_text = linkedtags(self.object.text)



        self.object.save()

        return HttpResponseRedirect(reverse_lazy('publicationdetail', kwargs = {'pk': self.object.pk}))

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    template_name = 'feed/publication_form.html'
    form_class = PublicationForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user

        self.object = form.save()
        if self.object.empty_img:
            self.object.img = None

        if self.object.empty_img2:
            self.object.img2 = None

        if self.object.empty_video:
            self.object.video = None

        if self.object.empty_pdf:
            self.object.pdf = None

        self.listtag = hastag(self.object.text)

        self.object.tags.clear()

        for self.tag in self.listtag:
            self.object.tags.add(self.tag)

        self.object.tag_text = linkedtags(self.object.text)


        self.object.save()

        print(self.object.tags)

        return HttpResponseRedirect(reverse_lazy('publicationdetail', kwargs = {'pk': self.object.pk}))

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publication
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationWCreateView(LoginRequiredMixin, CreateView):
    model = PublicationW
    template_name = 'feed/createw.html'
    form_class = PublicationWForm
    success_url = '/'

    def form_valid(self, form):

        form.instance.uname = self.request.user

        self.object = form.save()

        self.object.addresss = 'Colombia, ' + self.object.addresss


        location = geocoder.arcgis(self.object.addresss)
        if location.lat == None or location.lng == None:
            return HttpResponse('You address input is invalid')

        print('aquie es ', location)


        self.object.lat = location.lat
        self.object.lon = location.lng
        WarningMaps = folium.Map(location=[self.object.lat, self.object.lon], zoom_start=10)

        toolmark = "ALERTA" + " " + str(str(slugify(self.object.datatime))[:10] + " " + self.object.case_id)

        folium.Marker([self.object.lat, self.object.lon], tooltip=toolmark,
                      popup=self.object.description, icon=folium.Icon(color='yellow', icon='exclamation-triangle', prefix='fa')).add_to(WarningMaps)
        # Get HTML Representation of Map Object



        self.object.mapaddress = WarningMaps._repr_html_()

        listtag = hastag(self.object.description)

        for tag in listtag:
            self.object.involved.add(tag)

        print(self.object.involved)

        self.object.tag_text = linkedtags(self.object.description)

        self.object.tag_category, category =  categorytag(self.object.category)

        for tag2 in category:
            self.object.involved.add(tag2)

        self.object.save()


        return HttpResponseRedirect(reverse_lazy('publicationwdetail', kwargs = {'pk': self.object.pk}))


    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationWUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PublicationW
    template_name = 'feed/publicationw_form.html'
    form_class = PublicationWForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        self.object = form.save()


        if self.object.empty_img:
            self.object.img = None

        if self.object.empty_img2:
            self.object.img2 = None

        if self.object.empty_video:
            self.object.video = None

        if self.object.empty_pdf:
            self.object.pdf = None


        self.location = geocoder.arcgis(self.object.addresss)
        if self.location.lat == None or self.location.lng == None:
            return HttpResponse('You address input is invalid')


        self.object.lat = self.location.lat
        self.object.lon = self.location.lng

        WarningMaps = folium.Map(location=[self.object.lat, self.object.lon ], zoom_start=10)

        toolmark = "ALERTA" + " " + str(str(slugify(self.object.datatime))[:10] + " " + self.object.case_id)

        folium.Marker([self.object.lat, self.object.lon], tooltip=toolmark,
                      popup=self.object.description, icon=folium.Icon(color='yellow', icon='exclamation-triangle', prefix='fa')).add_to(WarningMaps)
        # Get HTML Representation of Map Object



        self.object.mapaddress = WarningMaps._repr_html_()

        listtag = hastag(self.object.description)


        self.object.involved.clear()
        for tag in listtag:
            self.object.involved.add(tag)


        self.object.tag_text = linkedtags(self.object.description)

        self.object.tag_category, category =  categorytag(self.object.category)

        for tag2 in category:
            self.object.involved.add(tag2)

        self.object.save()

        return HttpResponseRedirect(reverse_lazy('publicationwdetail', kwargs = {'pk': self.object.pk}))


    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationWDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PublicationW
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationICreateView(LoginRequiredMixin, CreateView):
    model = PublicationI
    template_name = 'feed/createi.html'
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)


class PublicationIUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PublicationI
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class PublicationIDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PublicationI
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True
