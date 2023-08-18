from django.urls import path

from .views import All_transaction, Select_transaction

urlpatterns = [
    path('', All_transaction.as_view(), name='all_transaction'),
    path('<int:id>/', Select_transaction.as_view(), name='select_transaction')
]