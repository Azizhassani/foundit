from django.urls import path
from .views import index,add_lost_item,register

urlpatterns = [
    path('lost-items/', index, name='lost_items_list'),
    path('add-lost-item/',add_lost_item, name='add_lost_item'),
    path('register/',register,name='register'),
]
