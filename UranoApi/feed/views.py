from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'feed/home.html'
    ordering = ['-datatime']


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'feed/create.html'
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form. instance.uname = self.request.user
        return super().form_valid(form)


class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tweet
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form. instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tweet
    success_url = '/'

    def form_valid(self, form):
        form. instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet = self.get_object()
        if self.request.user == tweet.uname:
            return True
        return True

