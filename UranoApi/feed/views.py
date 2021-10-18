from django.shortcuts import render
from .models import Publication, PublicationW, PublicationI
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .forms import PublicationForm, PublicationWForm, PublicationIForm
from taggit.models import Tag, slugify
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.urls import reverse
import pandas as pd
import folium
import geocoder


from django.http import HttpResponseRedirect


def hastag(text):
    hashtag_list = []

    if text:

        for word in text.split():
            if word[0] == '#':
                hashtag_list.append(word[1:])

    return hashtag_list


class PublicationDetail(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'feed/publication_detail.html'


class PublicationWDetail(LoginRequiredMixin, DetailView):
    model = PublicationW
    template_name = 'feed/publicationw_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        publications = context['publicationw']
        WarningMaps = folium.Map(location=[publications.lat, publications.lon], zoom_start=10)

        toolmark = "Advertencia" + " " + str(str(slugify(publications.datatime))[:10] + " " + publications.case_id)

        folium.Marker([publications.lat, publications.lon], tooltip=toolmark,
                      popup=publications.description).add_to(WarningMaps)
        # Get HTML Representation of Map Object
        warningmaps = WarningMaps._repr_html_()
        context['map'] = warningmaps

        return context


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/home.html'
    ordering = ['datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        warningmaps = []

        for publications in PublicationW.objects.all():
            WarningMaps = folium.Map(location=[publications.lat, publications.lon], zoom_start=10)

            toolmark = "Advertencia" + " " + str(str(slugify(publications.datatime))[:10] + " " + publications.case_id)

            folium.Marker([publications.lat, publications.lon], tooltip=toolmark,
                          popup=publications.description).add_to(WarningMaps)
            # Get HTML Representation of Map Object

            warningmaps.append(WarningMaps._repr_html_())

        warningmaps = zip(PublicationW.objects.all(), warningmaps)

        context['publicationt'] = Publication.objects.all()
        context['publicationw'] = warningmaps
        context['publicationi'] = PublicationI.objects.all()

        return context


class PublicationTagsView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/home.html'

    ordering = ['datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        warningmaps = []

        for publications in PublicationW.objects.filter(involved__slug=self.kwargs.get('tag_slug')):
            WarningMaps = folium.Map(location=[publications.lat, publications.lon], zoom_start=10)

            toolmark = "Advertencia" + " " + str(str(slugify(publications.datatime))[:10] + " " + publications.case_id)

            folium.Marker([publications.lat, publications.lon], tooltip=toolmark,
                          popup=publications.description).add_to(WarningMaps)
            # Get HTML Representation of Map Object

            warningmaps.append(WarningMaps._repr_html_())

        warningmaps = zip(PublicationW.objects.filter(involved__slug=self.kwargs.get('tag_slug')), warningmaps)
        context['publicationt'] = Publication.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
        context['publicationw'] = warningmaps
        context['publicationi'] = PublicationI.objects.all

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

        return HttpResponseRedirect(self.get_success_url())

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
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.listtag = hastag(self.object.text)

        for self.tag in self.listtag:
            self.object.tags.add(self.tag)

        print(self.object.tags)

        return HttpResponseRedirect(self.get_success_url())

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

    success_url = '/'
    form_class = PublicationWForm

    def form_valid(self, form):
        form.instance.uname = self.request.user
        self.object = form.save()
        self.location = geocoder.arcgis(self.object.address)
        if self.location.lat == None or self.location.lng == None:
            return HttpResponse('You address input is invalid')

        print('aquie es ', self.location)

        self.object.lat = self.location.lat
        self.object.lon = self.location.lng

        print(self.object.lat)
        print(self.location)

        self.listtag = hastag(self.object.description)

        for self.tag in self.listtag:
            self.object.involved.add(self.tag)

        print(self.object.involved)

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

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
        self.location = geocoder.arcgis(self.object.address)
        if self.location.lat == None or self.location.lng == None:
            return HttpResponse('You address input is invalid')

        print('aquie es ', self.location)

        self.object.lat = self.location.lat
        self.object.lon = self.location.lng
        self.object.country = self.location.country

        print(self.object.lat)
        print(self.location)

        self.listtag = hastag(self.object.description)

        for self.tag in self.listtag:
            self.object.involved.add(self.tag)

        print(self.object.involved)

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

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
