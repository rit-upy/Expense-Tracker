from django.urls import path
from .views import LogInView, Logout, SignUpAPIView

urlpatterns = [
    path('login/', LogInView.as_view(), name='api_login'),
    path('logout/', Logout.as_view(), name='api_logout'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
]
