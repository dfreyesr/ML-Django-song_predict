from django.urls import path
from .views import predict_success
from .views import predict_form

urlpatterns = [
    path('', predict_form, name="predict_form"),
    path('predict/', predict_success, name="predict_success"),
]