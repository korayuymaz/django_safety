from django.urls import path

from . import views

urlpatterns = [
    path('', views.nonconformity_tracking, name='overview'),
    path('<int:pk>/', views.nonconformity_reporting, name='create_nonconformity'),
    path('employee/', views.all_employee, name='employee_overview'),
    path('employee/<int:pk>/', views.new_employee, name='create_employee'),
]
