from django.conf.urls import url
from .import views
from accounts.views import LandingPageView
from django.contrib.auth.views import login, logout, password_reset, password_reset_done
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    url(r'^login$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change-password'),
    url(r'^reset-password$', password_reset, name='reset_password'),
    url(r'^reset_password_done$', password_reset_done, name='password_reset')

]
