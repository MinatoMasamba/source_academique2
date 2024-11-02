from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    
class ProfileForm(forms.ModelForm):
    PROMOTION_CHOICES = [
        ('PREPA', 'Préparation'),
        ('L1', 'Licence 1'),
        # Ajoute d’autres choix ici si nécessaire
    ]
    promotion = forms.ChoiceField(choices=PROMOTION_CHOICES)
    class Meta:
        model = Profile
        fields = [ 'promotion','first_name','last_name','numero_whatsapp','photo']


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    # Vous pouvez personnaliser les widgets si besoin
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Numéro de téléphone, nom d\'utilisateur ou e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
