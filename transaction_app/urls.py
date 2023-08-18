from django.urls import path

from .views import All_transaction

urlpatterns = [
    path('', All_transaction.as_view(), name='all_transaction'),
]