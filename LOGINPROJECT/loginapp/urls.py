from django.urls import path
from .import views

urlpatterns = [path("sub",views.registering),
               path("login",views.logging),
               path("forgot",views.forgotting)]
    