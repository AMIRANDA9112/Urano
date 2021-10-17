from django.forms import Form, ModelForm
from django.forms.models import inlineformset_factory

from .models import Publication, PublicationW, PublicationI


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['text', 'img', 'img2', 'video', 'pdf']


class PublicationWForm(ModelForm):
    class Meta:
        model = PublicationW
        fields = ['case_id', 'description', 'involved', 'address', 'img', 'img2', 'video', 'pdf']


class PublicationIForm(ModelForm):
    class Meta:
        model = PublicationI
        fields = ['text']



