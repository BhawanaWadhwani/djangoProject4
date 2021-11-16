from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from cardmaker.views import show_all_decks
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# Create your views here.
def signup(request):
    if request.method == "GET":
        form = RegistrationForm()

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists, please try another username")
            return redirect('/')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email ID already registered, please try another Email ID")
            return redirect('/')

        if password != password1:
            messages.error(request, "Password and Confirm Password did not match, please try again")
            return redirect('/')

        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = True
        new_user.save()
        return redirect('/')

    return render(request, 'signup.html', {'form': form})