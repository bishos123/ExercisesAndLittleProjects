"""
URL configuration for exercisesWebSiteRapha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from webSiteRapha import views

urlpatterns = [
    path('band-name/', views.band_name, name='band_name'),
    path('tip-calculator/', views.tip_calculator, name='tip_calculator'),
    path('even_odd/', views.even_odd, name='even_odd'),
    path('r_p_s/', views.r_p_s, name='r_p_s'),
    path('', views.home, name='home')
]
