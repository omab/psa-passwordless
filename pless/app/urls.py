from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('passwordless.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)
