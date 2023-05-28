from django.urls import path,include
from . import views
urlpatterns = [
    path('portfolio/', views.index,name='index'),
    path('', views.home,name='home'),
    path('register/',views.register, name = 'register'),
    path('login/',views.loginPage, name = 'login'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.indexT,name='indexT'),
    path('about/',views.indexP,name='indexP'),
    path('service/',views.service,name='service'),
    path('booking/',views.booking,name='booking'),
    path('profile/',views.profile,name='profile'),
    path('portfolio/Avis/',views.AvisC,name='Avis'),
 ]