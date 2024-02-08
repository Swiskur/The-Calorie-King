from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search),
    path('counter/', views.counter),
    path('results/', views.results),
    path('contact/', views.contact),
    path('signup/', views.sign_up, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

]