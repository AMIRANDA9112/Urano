from django.shortcuts import render
from .models import Publication, PublicationW, PublicationI
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from taggit.models import Tag
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
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


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/home.html'
    ordering = ['-datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        warningmaps = []

        for publications in PublicationW.objects.all():


            WarningMaps = folium.Map(location=[publications.lat, publications.lon], zoom_start=10)

            folium.Marker([publications.lat, publications.lon], tooltip='Click for more',
                          popup=publications.country).add_to(WarningMaps)
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

    ordering = ['-datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['publicationt'] = Publication.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
        context['publicationw'] = PublicationW.objects.filter(involved__slug=self.kwargs.get('tag_slug'))
        context['publicationi'] = PublicationI.objects.all

        return context


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'feed/create.html'
    fields = ['text', 'img', 'img2', 'video', 'pdf']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        self.object = form.save()

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


class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    template_name = 'feed/publication_form.html'
    fields = ['text', 'img', 'img2', 'video', 'pdf']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        self.object = form.save()

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
    fields = ['case_id', 'description', 'involved', 'address', 'img', 'img2', 'video', 'pdf']
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


class PublicationWUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PublicationW
    template_name = 'feed/publicationw_form.html'
    fields = ['case_id', 'description', 'involved', 'address', 'img', 'img2', 'video', 'pdf']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        self.object = form.save()

        self.listtag = hastag(self.object.description)

        for self.tag in self.listtag:
            self.object.involved.add(self.tag)

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
