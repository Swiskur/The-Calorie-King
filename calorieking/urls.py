from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search),
    path('burnersearch/', views.burner_search),
    path('counter/', views.counter),
    path('burnercounter/', views.burner_counter),
    path('results/', views.results),
    path('contact/', views.contact),
    path('burnerresults/', views.burner_results),
    path('signup/', views.sign_up, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

]