from django.urls import path
from . import views

urlpatterns = [
    path("splash", views.splash, name="splash"),
    path("home/", views.home, name="home"),
    path("nav/", views.navigation, name="navigation"),
    path("footer/", views.footer, name="footer"),
    path("sotuvchi_bolish/", views.sotuvchi_bolish, name="sotuvchi"),
    path("sotuvchi_login/", views.sotuvchi_login, name="sotuvchi_login"),
    path("sotuvchi_register/", views.sotuvchi_register, name="sotuvchi_register"),
    path("topshirish_punkitini_ochish/", views.topshirish_punkitini_ochish, name="topshirish_punkitini_ochish"),
    path("savol/", views.savol_javob, name="savol_javob"),
    path("salom/", views.salom, name="salom"),
    path("savdo/", views.savdo, name="savdo"),
    path("detail/<int:tovar_id>/", views.detail, name="detail"),
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
]
