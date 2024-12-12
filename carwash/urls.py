"""
URL configuration for CarWashingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your Django project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from .views import  *
urlpatterns = [
    path('admin/', admin.site.urls),
    ### swager
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ### documentation
    path('documentation/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ###

    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('work_logs/', WorkLogListCreateAPIView.as_view(), name='worklog-list-create'),
    path('work_logs/<int:pk>/', WorkLogDetailAPIView.as_view(), name='worklog-detail'),
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('licenses/', LicenseListCreateAPIView.as_view(), name='license-list-create'),
    path('licenses/<int:pk>/', LicenseDetailAPIView.as_view(), name='license-detail'),
    path('warranties/', WarrantyListCreateAPIView.as_view(), name='warranty-list-create'),
    path('warranties/<int:pk>/', WarrantyDetailAPIView.as_view(), name='warranty-detail'),
    path('appointments/', AppointmentListCreateAPIView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailAPIView.as_view(), name='appointment-detail'),
    path('car-clinics/', CarClinicListCreateAPIView.as_view(), name='car-clinic-list-create'),
    path('car-clinics/<int:pk>/', CarClinicDetailAPIView.as_view(), name='car-clinic-detail'),
]
