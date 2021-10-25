from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Nombre de Usuario'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Contraseña'}

    )


class MailsPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Correo de Recuperación',
                                                                }
        )


class ResetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Ingrese su Contraseña Nueva',
                                                                }
        )
        self.fields['new_password2'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Confirme su Contraseña Nueva',
                                                                }
        )




class CustomChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Contraseña Antigua'}
        )
        self.fields['new_password1'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Contraseña Nueva'}
        )
        self.fields['new_password2'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Confirme Contraseña Nueva'}
        )



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


        widgets = { 'username' : forms.TextInput(attrs={'class' : 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Nombre de Usuario'}),
                    'first_name' : forms.TextInput(attrs={'class' : 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Nombres'}),
                    'last_name' : forms.TextInput(attrs={'class' : 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Apellidos'}),
                    'email' : forms.EmailInput(attrs={'class' : 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Correo Electronico'}),

                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Contraseña'}
        )
        self.fields['password2'].widget.attrs.update(
          {'class': 'bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'placeholder':'Confirmar Contraseña'}
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
        widgets = { 'image' : forms.FileInput(attrs={'id':'hidden-input', 'class':'hidden z-10'}),
                    'bio' : forms.Textarea(attrs={'class' : 'rounded bg-gray-700 text-gray-100 placeholder-blue-100 w-full', 'rows':'4', 'cols':'40', 'placeholder':'Cuentanos de Ti'}),
                    }



























