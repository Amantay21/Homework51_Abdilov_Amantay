from django.urls import path, include
from webapp.views import index, action

urlpatterns = [
    path('', index),
    path('action/', action)
]
