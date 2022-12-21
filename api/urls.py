from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

urlpatterns = [
    path("rediredct/", views.RedirectViewSet.as_view(), name="clientes"),

]
