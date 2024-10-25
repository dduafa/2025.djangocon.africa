from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.page_home, name="page_home"),
    path("team/", views.page_team, name="page_team"),
]
