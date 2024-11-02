from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Cours, Interro, Examen, TP, Note,Profile,Message
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,ProfileForm
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def accueil(request):
    """Affiche les cours disponibles par promotion pour les utilisateurs connectés."""
    promotion = request.user.profile.promotion  # Supposons que vous ayez un modèle Profile lié à l'utilisateur
    cours = Cours.objects.filter(promotion=promotion)
    return render(request, 'source_polytechnique/accueil.html', {
        'cours': cours,
        'promotion': promotion,
    })

@login_required
def cours_detail(request, promotion):
    """Affiche les détails des cours pour une promotion spécifique."""
    cours = Cours.objects.filter(promotion=promotion)
    return render(request, 'source_polytechnique/cours_detail.html', {
        'cours': cours,
        'promotion': promotion,
    })


@login_required
def interros(request):
    """Affiche les interros disponibles pour la promotion de l'utilisateur connecté."""
    promotion = request.user.profile.promotion
    interros = Interro.objects.filter(promotion=promotion)
    return render(request, 'interros.html', {
        'interros': interros,
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def register(request):
    """Permet aux utilisateurs de s'inscrire."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password1')  # Assurez-vous d'utiliser le bon champ ici

            if User.objects.filter(email=email).exists():
                messages.error(request, "L'adresse email existe déjà dans la base de données.")
                return render(request, 'register.html', {'user_form': user_form})

            # Créez l'utilisateur avec le mot de passe haché
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()  # Sauvegarder l'utilisateur dans la base de données

            messages.success(request, "Votre compte a été créé avec succès!")
            return redirect('accueil')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'register.html', {'user_form': user_form})

def ExemViexs(request):
    """ Afficher touot les examen si l'utilisateur n'est pas connecter """
    if request.user.is_authenticated:
            profil = Profile.objects.get(user=request.user)
            user_promotion = profil.promotion
            exam = Examen.objects.filter(promotion = user_promotion)
    else:
        exam = None
        return redirect('accueil')
    context = {
        'exam':exam
    }
    return render(request,'exam.html',context)

def InterroViexs(request):
    """ Afficher touot les examen si l'utilisateur n'est pas connecter """
    if request.user.is_authenticated:
            profil = Profile.objects.get(user=request.user)
            user_promotion = profil.promotion
            interros = Interro.objects.filter(promotion = user_promotion)
    else:
        interros = None
        return redirect('accueil')
    context = {
        'interros':interros
    }
    return render(request,'interro.html',context)

def NoteViexs(request):
    """ Afficher touot les examen si l'utilisateur n'est pas connecter """
    if request.user.is_authenticated:
            profil = Profile.objects.get(user=request.user)
            user_promotion = profil.promotion
            notes = Note.objects.filter(promotion = user_promotion)
    else:
        notes = None
        return redirect('accueil')
    context = {
        'notes':notes
    }
    return render(request,'note.html',context)

def TpViexs(request):
    """ Afficher touot les examen si l'utilisateur n'est pas connecter """
    if request.user.is_authenticated:
            profil = Profile.objects.get(user=request.user)
            user_promotion = profil.promotion
            tps = TP.objects.filter(promotion = user_promotion)
    else:
        tps = None
        return redirect('accueil')
    context = {
        'tps':tps
    }
    return render(request,'tp.html',context)


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile(request):
    # Récupérer ou créer le profil de l'utilisateur connecté
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Votre profil a été mis à jour avec succès.")
            return redirect('profile')
        else:
            # Afficher les erreurs du formulaire dans la console
            print("Formulaire invalide :", form.errors)
            messages.error(request, "Une erreur est survenue lors de la mise à jour.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})


from django.shortcuts import render
from .models import Profile, Cours, Message
    # Définir la liste des matières par défaut
def matieres_defaut():
        return [
            {"nom": "Algebre Lineaire", "heures_cours": 60, "heures_tp": 60},
            {"nom": "Physique", "heures_cours": 75, "heures_tp": 60},
            {"nom": "Analyse Math", "heures_cours": 60, "heures_tp": 60},
            {"nom": "Geometrie Analytique et plan", "heures_cours": 45, "heures_tp": 45},
            {"nom": "Calcul Numerique et Trigo", "heures_cours": 30, "heures_tp": 30},
            {"nom": "Dessin Technique", "heures_cours": 15, "heures_tp": 30},
            {"nom": "Geometrie Descriptive", "heures_cours": 30, "heures_tp": 30},
            {"nom": "Anglais", "heures_cours": 25, "heures_tp": 10},
            {"nom": "Français", "heures_cours": 30, "heures_tp": 0},
            {"nom": "Informatique", "heures_cours": 25, "heures_tp": 10},
            {"nom": "Chimie", "heures_cours": 45, "heures_tp": 45}
        ]
def matieres_defaut1():
        return [
                {"nom": "Education a la citoyenneté", "heures_cours": 30, "heures_tp": 0},
                {"nom": "Physique", "heures_cours": 75, "heures_tp": 60},
                {"nom": "Logique et expression orale et ecrit en fr", "heures_cours": 15, "heures_tp": 0},
                {"nom": "Introduction à l'infomatique", "heures_cours": 30, "heures_tp": 0},
                {"nom": "Algebre lineaire et calcul vectoriel", "heures_cours": 60, "heures_tp": 60},
                {"nom": "Analyse infinitesimale et geo diferentielle", "heures_cours": 60, "heures_tp": 60},
                {"nom": "Statique appliquée", "heures_cours": 30, "heures_tp": 30},
                {"nom": "Physique generale", "heures_cours": 90, "heures_tp": 75},
                {"nom": "Chimie genrale", "heures_cours": 45, "heures_tp": 45},
                {"nom": "Mecanique rationnelle 1", "heures_cours": 30, "heures_tp": 30},
                {"nom": "Dessin industriel", "heures_cours": 15, "heures_tp": 30}
            ]
def home(request):
    """" Affiche les informations de tous les cours si l'utilisateur n'est pas connecté """

    matieres = None 
    list_etudiant = None  # Initialiser list_etudiant en tant que None

    if request.user.is_authenticated:
        profil = Profile.objects.get(user=request.user)
        user_promotion = profil.promotion
        cours = Cours.objects.filter(promotion=user_promotion)
        list_etudiant = Profile.objects.filter(promotion=user_promotion)
        if user_promotion == 'PREPA':
             matieres = matieres_defaut()  # Initialiser les matières par défaut pour tous les utilisateurs
        else:
            matieres = matieres_defaut1()
    else:
        cours = Cours.objects.all()

    messages = Message.objects.all()  # Récupérer tous les messages

    # Contexte pour le rendu
    context = {
        'matieres': matieres,
        'cours': cours,
        'list_etudiant': list_etudiant,
        'messages_admin': messages,
    }
    
    return render(request, "accueil.html", context)


def login_view(request):
    """Permet aux utilisateurs de se connecter à leur compte existant."""
    if request.method == 'POST':
        
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print('connecter')
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes connecté avec succès!')
                return redirect('accueil')  # Assurez-vous que 'accueil' est défini dans vos URLs
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = CustomLoginForm()
        messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        print('sa ne mache pas ')


    return render(request,'login.html', {'form': form})


def logout_view(request):
    """Permet aux utilisateurs de se déconnecter de leur compte."""
    logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès!')
    return redirect('accueil')  # Redirigez vers la page de connexion ou une autre page

