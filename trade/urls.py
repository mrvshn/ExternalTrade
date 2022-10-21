from django.urls import path, include
from trade.views import contact, homepage

urlpatterns = [
    path('', homepage),
    path('contact', 'contact', name='contact'),
]
