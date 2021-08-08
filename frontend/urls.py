from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("edit/<str:status_uuid>", views.edit, name="edit"),
    path("detail/<str:status_uuid>", views.detail, name="detail")
]
