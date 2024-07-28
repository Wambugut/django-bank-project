from django.urls import path
from .views import register, login_view, logout_view, view_profile, edit_profile, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', view_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]


