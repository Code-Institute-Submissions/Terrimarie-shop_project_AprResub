from django.urls import path
from . import views
# code from boutique ado project
urlpatterns = [
    path('', views.index, name='home')
]
