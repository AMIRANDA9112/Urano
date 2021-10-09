from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Publication, ImgPublication, VideoPublication, PdfPublication


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['text']


class ImgPublicationForm(ModelForm):
    class Meta:
        model = ImgPublication
        fields = ['img']


class VideoPublicationForm(ModelForm):
    class Meta:
        model = VideoPublication
        fields = ['video']


class PdfPublicationForm(ModelForm):
    class Meta:
        model = PdfPublication
        fields = ['pdf']


ImgFormSet = inlineformset_factory(Publication, ImgPublication, form=ImgPublicationForm, extra=1, max_num=2)
VideoFormSet = inlineformset_factory(Publication, VideoPublication, form=VideoPublicationForm, max_num=1)
PdfFormSet = inlineformset_factory(Publication, PdfPublication, form=PdfPublicationForm, max_num=1)
