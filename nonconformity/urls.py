from django.urls import path
from .views import NonconformityListView, NonconformityDetailView, NonconformityCreateView
from . import views

app_name = 'nonconformity'

urlpatterns = [
    path('', NonconformityListView.as_view(), name='overview'),
    path('<int:pk>/', NonconformityDetailView.as_view(), name='detail'),
    path('new/', NonconformityCreateView.as_view(), name='create'),
]

# nonconformity/nonconformity_
