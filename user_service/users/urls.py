from django.urls import path
from .views import RegisterView, PasswordResetRequestView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('register/', csrf_exempt(RegisterView.as_view()), name='register'),
    path('request-password-reset/', PasswordResetRequestView.as_view(), name='request-password-reset'),
]