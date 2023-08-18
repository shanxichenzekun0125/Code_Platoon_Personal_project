from django.urls import path

from .views import All_category

urlpatterns = [
    path('', All_category.as_view(), name='all_category'),
]