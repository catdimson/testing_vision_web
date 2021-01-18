from django.urls import path
from .views import base_view
from rest_framework.routers import DefaultRouter

from .views import CustomUserListCreateView, CustomUserDetailView

urlpatterns = [
    path('', base_view, name='base_view'),
    path("api/accounts/all-profiles", CustomUserListCreateView.as_view(), name="all-profiles"),
    path("api/accounts/profile/<int:pk>", CustomUserDetailView.as_view(), name="profile"),
]