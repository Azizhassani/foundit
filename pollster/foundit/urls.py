from django.urls import path
from .views import index

urlpatterns = [
    path('lost-items/', index, name='lost_items_list'),
]
