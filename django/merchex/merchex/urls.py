"""
URL configuration for merchex project.

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

from django.contrib import admin
from django.urls import path
from listings import views
# je créé une copie de mon objet views listings
# pour pouvoir apporter plusieurs views
Vlistings = views
from viewsDistributeur import views
# je créé une copie de mon objet views viewsDistributeur
# pour pouvoir apporter plusieurs views
Vdistri = views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", Vlistings.hello),
    path("distri/", Vdistri.distri),
    path("about/", Vlistings.about),
    path("m2i/", Vlistings.m2i)
]
