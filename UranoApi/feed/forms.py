from django.forms import Form, ModelForm
from django.forms.models import inlineformset_factory
from django import forms

from .models import Publication, PublicationW, PublicationI, Comments, CommentsW






class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['text', 'img', 'img2', 'video', 'pdf','empty_img', 'empty_img2', 'empty_video', 'empty_pdf']
        widgets = { 'text' : forms.Textarea(attrs={'class' : 'text-xs rounded bg-gray-700 text-gray-100 placeholder-blue-100 w-full','rows':'5', 'cols':'40', 'placeholder':'Espacio de Libre Opinión'}),
            'img' : forms.FileInput(attrs={'id':'hidden-input', 'class':'hidden z-10'}),
            'img2' : forms.FileInput(attrs={'id':'hidden-input2', 'class':'hidden z-10'}),
            'video' : forms.FileInput(attrs={'id':'hidden-input3', 'class':'hidden z-10', "accept":"video/*"}),
            'pdf' : forms.FileInput(attrs={'id':'hidden-input4', 'class':'hidden z-10', "accept":"application/pdf"}),
            }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = { 'text' : forms.Textarea()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'text-xs rounded bg-gray-700 text-gray-100 placeholder-blue-100 w-full','rows':'3', 'cols':'40', 'placeholder':'Comentario de Libre Opinión'})


class CommentsWForm(ModelForm):
    class Meta:
        model = CommentsW
        fields = ['text']
        widgets = { 'text' : forms.Textarea(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'text-xs rounded bg-gray-700 text-gray-100 placeholder-blue-100 w-full','rows':'3', 'cols':'40', 'placeholder':'Comentario de Libre Opinión'})


class PublicationWForm(ModelForm):

    class Meta:
        model = PublicationW
        fields = ['case_id', 'description', 'addresss', 'img', 'img2', 'video', 'pdf', 'empty_img', 'empty_img2', 'empty_video', 'empty_pdf', 'category']
        widgets = { 'case_id' : forms.TextInput(attrs={'class' : 'text-sm rounded bg-gray-700 text-gray-100 placeholder-yellow-200 w-full', 'placeholder':'Titulo de Alerta'}),

            'description' : forms.Textarea(attrs={'class' : 'text-xs rounded bg-gray-700 text-gray-100 placeholder-yellow-200 w-full','rows':'3', 'cols':'40', 'placeholder':'Describa a detalle la Alerta'}),

            'addresss' : forms.Textarea(attrs={'class' : 'text-xs rounded bg-gray-700 text-gray-100 placeholder-yellow-200 w-full','rows':'2', 'cols':'40', 'placeholder':'Ingrese Ubicación - Ejemplo - Valle del Cauca, Cali, Ciudad Cordoba, calle 42 carrera 50'}),

            'img' : forms.FileInput(attrs={'id':'hidden-input', 'class':'hidden z-10'}),
            'img2' : forms.FileInput(attrs={'id':'hidden-input2', 'class':'hidden z-10'}),
            'video' : forms.FileInput(attrs={'id':'hidden-input3', 'class':'hidden z-10', "accept":"video/*"}),
            'pdf' : forms.FileInput(attrs={'id':'hidden-input4', 'class':'hidden z-10', "accept":"application/pdf"})}




class PublicationIForm(ModelForm):
    class Meta:
        model = PublicationI
        fields = ['text']



