from django.conf.urls import url
from bank.views import banking_page
from .import views
from bank.views import CreateCustomer, customer_profile
from django.conf.urls.static import static
from django.conf import settings

app_name = 'bank'


urlpatterns = [
    url(r'^$', views.banking_page, name='home'),
    url(r'^create-customer$', CreateCustomer.as_view(), name='create_customer'),
    url(r'^customer-profile$', views.customer_profile, name='customer_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)