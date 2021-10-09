from django.shortcuts import render
from .models import Publication, PublicationW, PublicationI
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import PublicationForm, ImgFormSet, VideoFormSet, PdfFormSet
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
    template_name = 'feed/create.html'
    model = Publication
    form_class = PublicationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        img_form = ImgFormSet()
        video_form = VideoFormSet()
        pdf_form = PdfFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  img_form=img_form,
                                  video_form=video_form,
                                  pdf_form=pdf_form
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        img_form = ImgFormSet(self.request.POST)
        video_form = VideoFormSet(self.request.POST)
        pdf_form = PdfFormSet(self.request.POST)
        if (form.is_valid() and img_form.is_valid() and
                video_form.is_valid() and pdf_form.is_valid()):
            return self.form_valid(form, img_form, video_form, pdf_form)
        else:
            return self.form_invalid(form, img_form, video_form, pdf_form)

    def form_valid(self, form, img_form, video_form, pdf_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.uname = self.request.user
        self.object = form.save()
        img_form.instance = self.object
        img_form.save()
        video_form.instance = self.object
        video_form.save()
        pdf_form.instance = self.object
        pdf_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, img_form, video_form, pdf_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  img_form=img_form,
                                  video_form=video_form,
                                  pdf_form=pdf_form
                                  ))


class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
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
