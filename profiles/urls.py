from django.urls import path
from . import views
# code taken from boutique abo project
urlpatterns = [
    path('', views.profile, name='profile')
]
