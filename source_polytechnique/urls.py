
from .views import register,profile,home,ExemViexs,InterroViexs,TpViexs,NoteViexs,login_view,logout_view
from django.urls import path

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('note/',NoteViexs,name='note'),
    path('tp/',TpViexs,name='tp'),
    path('interro/',InterroViexs,name='interro'),
    path('examen/',ExemViexs,name='exam'),
    path('',home,name='accueil'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    # ... autres URLs
]
