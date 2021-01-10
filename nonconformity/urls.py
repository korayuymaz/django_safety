from django.urls import path
from .views import (NonconformityListView, NonconformityDetailView, NonconformityCreateView,
                    NonconformityUpdateView, NonconformityDeleteView)
from . import views

app_name = 'nonconformity'

urlpatterns = [
    path('', NonconformityListView.as_view(), name='overview'),
    path('<int:pk>/', NonconformityDetailView.as_view(), name='detail'),
    path('new/', NonconformityCreateView.as_view(), name='create'),
    path('<int:pk>/update', NonconformityUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', NonconformityDeleteView.as_view(), name='delete'),
]

# nonconformity/nonconformity_
