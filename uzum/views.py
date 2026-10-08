from django.shortcuts import render, get_object_or_404, redirect
from .models import Kit
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='register')
def home(request):
    kit = Kit.objects.all()
    return render(request, "home.html", {"kit": kit})


def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")


def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")


def sotuvchi_login(request):
    return render(request, "sotuvchi_login.html")


def sotuvchi_register(request):
    return render(request, "sotuvchi_register.html")


def topshirish_punkitini_ochish(request):
    return render(request, "topshirish_punkitini_ochish.html")


def savol_javob(request):
    return render(request, "savol_javob.html")


def salom(request):
    return render(request, "salom.html")


def savdo(request):
    return render(request, "savdo.html")


def splash(request):
    return render(request, "splash.html")

def login(request):
    return render(request, "login.html") 


def detail(request, tovar_id):
    kit = get_object_or_404(Kit, id=tovar_id)
    context = {
        "kit": kit
    }

    return render(request, "detail.html", context)








def register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            auth_login(request, user)
            messages.error(request, "Parollar bir xil emas!")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username allaqachon mavjud!")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan!")
            return redirect("register")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("home")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.error(
                request,
                "Iltimos, foydalanuvchi nomini kiriting"
            )
            return redirect('login')

        try:
            user = User.objects.get(username=username)

            if user.is_superuser:
                auth_login(request, user)
                logger.info("Admin tizimga kirdi")
                return redirect('home')
            else:
                if not password:
                    logger.warning(
                        f"{username}, login qilishda Nolum xato"
                    )
                    return redirect('login')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                auth_login(request, user)
                messages.success(
                    request,
                    "Siz muvaffaqiyatli tizimga kirdingiz"
                )
                return redirect('home')
            else:
                logger.warning(
                    f"{username} login qilishda Nolum xato"
                )

        except User.DoesNotExist:
            messages.error(
                request,
                "Bunday foydalanuvchi mavjud emas"
            )
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect("home")