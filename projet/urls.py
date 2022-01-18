"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import  page.views

urlpatterns = [
    path('contact',page.views.contact, name='contact'),
    path('service', page.views.service, name='service'),
    path('project', page.views.projet, name='project'),
    path('feature', page.views.feature, name='feature'),
    path('quote', page.views.quote, name='quote'),
    path('team', page.views.team, name='team'),
    path('testimonial', page.views.testimonial, name='testimonial'),
    path('404', page.views.quatre, name='404'),

    path('about', page.views.about, name='about'),
    path('home',page.views.index,name='home'),
    path('admin/', admin.site.urls),
]
