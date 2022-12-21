from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

urlpatterns = [
    path("ordenes/", views.OdersViewSet.as_view(), name="Ordenes"),
    path("ordenes/<str:idOrder>", views.OderViewSet.as_view(), name="Ordenes"),
    path("ordendetail/", views.OdersDetailsViewSet.as_view(), name="Detalles De Orden"),
    path("ordendetail/<str:idOrder>", views.OderDetailsViewSet.as_view(), name="Detalles De Orden"),
]