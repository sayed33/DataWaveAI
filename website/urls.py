
from django.urls import path
from . import views
from .views import about_view, contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about_view, name='about'),
    path('services/', views.services, name='services'),
    path('test/', views.test, name='test'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('packages/<str:category_slug>/', views.packages_by_category, name='packages_by_category'),
    path('contact/', contact_view, name='contact'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
]
