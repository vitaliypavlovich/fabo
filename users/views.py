import logging


from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import RegisterUserForm, LoginForm
from users.models import User

logger = logging.getLogger(__name__)


from django.contrib.auth import logout, login, authenticate

def index(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Users view")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/login/")
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("/admin/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})