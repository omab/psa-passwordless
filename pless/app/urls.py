from django.urls import include, path


urlpatterns = [
    path(r'', include('passwordless.urls')),
    path(r'', include('social_django.urls', namespace='social')),
]
