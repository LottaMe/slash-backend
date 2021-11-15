from django.urls import include, path

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]