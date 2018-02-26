from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [

    path('', views.index_courses, name='index_courses'),
    path('detalhes/<slug:slug>/', views.details, name='details'),
]