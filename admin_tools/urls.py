from django.conf.urls import url
from django.views.generic import TemplateView

from admin_tools import views

urlpatterns = [
    url(r'^reports/submit/$', views.submit, name='reports.submit'),
    url(r'^reports/invoices/$', views.invoice_report, name='reports.invoices'),
]
