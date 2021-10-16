from django.shortcuts import render
from .models import Publication, PublicationW, PublicationI
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'feed/home.html'
    ordering = ['-datatime']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['publicationw'] = PublicationW.objects.all()
        context['publicationi'] = PublicationI.objects.all()
        return context


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'feed/create.html'
    fields = ['text', 'img', 'img2', 'video', 'pdf']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

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
        return super().form_valid(form)

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
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)


class PublicationWUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PublicationW
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
