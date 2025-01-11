# autenticacion/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    barrio = forms.CharField(max_length=100, label='Barrio')
    direccion = forms.CharField(max_length=255, label='Dirección')
    telefono = forms.CharField(max_length=20, label='Teléfono')

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Las contraseñas no coinciden.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            # Asignar los campos del perfil
            UserProfile.objects.create(
                user=user,
                barrio=self.cleaned_data['barrio'],
                direccion=self.cleaned_data['direccion'],
                telefono=self.cleaned_data['telefono'],
            )
        return user
