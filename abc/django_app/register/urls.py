from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('register/', views.registerPage, name="register"),
   # path('login/',),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    #path('logout/'),


]