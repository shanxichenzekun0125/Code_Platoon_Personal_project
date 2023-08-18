from django.urls import path
from .views import Sign_up, Log_in

urlpatterns = [

    path('signup/', Sign_up.as_view(), name='signup'),
    path('login/', Log_in.as_view(), name='signup'),

]