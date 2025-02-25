from django.urls import path
from .views import index,add_lost_item,register,user_login,user_logout

urlpatterns = [
    path('lost-items-list/', index, name='lost_items_list'),
    path('add-lost-item/',add_lost_item, name='add_lost_item'),
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
]
