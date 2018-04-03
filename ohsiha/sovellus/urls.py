from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import logout, login


urlpatterns = [
    path('', views.index, name='index'),
    path('testi', views.testi, name='testi'),
    path('kirjautuminen/',	views.kirjautuminen,	name='kirjautuminen'),
    path('login/', login, name='login'),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]
