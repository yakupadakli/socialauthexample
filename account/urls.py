from django.conf.urls import url, include

from account.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    # Url Entries for social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Url Entries for django administration
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
