from django.urls import path
from django.contrib.auth.views import login, logout

from . import views

app_name = 'acounts'
urlpatterns = [

    path('', views.dashboard , name='dashboard'),
    path('editar', views.edit , name='edit'),
    path('editar-senha', views.edit_password , name='edit_password'),
    path('comfirma-nova-senha/<str:key>/', views.password_reset_confirm , name='password_reset_confirm'),
    path('entra/', login,{'template_name':'acounts/login.html'} , name='login'),
    path('cadastra-se/', views.register , name='register'),
    path('recuperar-senha/', views.password_reset , name='password_reset'),
    path('sair/', logout,{'next_page':'core:home'} , name='logout'),
]