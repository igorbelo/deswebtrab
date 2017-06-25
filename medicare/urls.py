"""medicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from website import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/?', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^services/?', TemplateView.as_view(template_name='services.html'), name='services'),
    url(r'^contact/?', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^signup/?', TemplateView.as_view(template_name='signup.html'), name='signup'),
    url(r'^supplier_signup/?', views.SupplierSignUpView.as_view(), name='supplier_signup'),
    url(r'^customer_signup/?', views.CustomerSignUpView.as_view(), name='customer_signup'),
    url(r'^book/?', views.BookView.as_view(), name='book'),
    url(r'^donate/?', views.DonateView.as_view(), name='donate'),
    url(r'^login/?', views.LoginView.as_view(), name='login'),
    url(r'^logout/?', views.LogoutView.as_view(), name='logout'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home')
]
