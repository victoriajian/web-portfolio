from django.urls import path
from . import views

urlpatterns = [
    path("", views.work_overview, name="work_overview"),
    path("<int:pk>/", views.work_detail, name="work_detail"),
]