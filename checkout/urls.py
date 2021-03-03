from django.urls import path
from . import views
# Some code here taken from boutique ado project
urlpatterns = [
    path('', views.checkout, name='checkout')
]