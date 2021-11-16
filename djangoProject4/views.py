from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.utils.encoding import force_bytes
from .tokens import generate_token
from djangoProject4 import settings



def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user2 = User.objects.get(email=email)
        subject = "Password Reset Requested"
        email_template_name = "password/password_reset_email.txt"
        c = {
            #  user.email,
            "email": request.POST.get('from_email', ''),
            'domain': '127.0.0.1:8000',
            'site_name': 'Website',
            "uid": urlsafe_base64_encode(force_bytes(user2.pk)),
            "user": user2,
            'token': default_token_generator.make_token(user2),
            'protocol': 'http',
        }
        email = render_to_string(email_template_name, c)
        to_list = [request.POST['email']]
        try:
            send_mail(subject, email, settings.EMAIL_HOST_USER, to_list, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


