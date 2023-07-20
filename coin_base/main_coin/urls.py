from django.urls import path
from .views import СurrencyView

urlpatterns = [
    path('', СurrencyView.as_view(), name='myview'),
]
