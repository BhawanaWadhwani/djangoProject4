from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='sign_up')

]
