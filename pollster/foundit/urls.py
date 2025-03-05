from django.urls import path
from .views import index,add_lost_item,register,user_login,user_logout,edit_lost_item,user_lost_items,delete_lost_item

urlpatterns = [
    path('lost-items-list/', index, name='lost_items_list'),
    path('add-lost-item/',add_lost_item, name='add_lost_item'),
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('my-lost-items/', user_lost_items, name='user_lost_items'),
    path('edit/<int:item_id>/', edit_lost_item, name='edit_lost_item'),
    path('delete/<int:item_id>/', delete_lost_item, name='delete_lost_item'),


]
