from django.contrib import admin
from .models import Founditem,User,LostItem,FoundItemRequest
# Register your models here.

admin.site.register(Founditem)
admin.site.register(LostItem)
admin.site.register(User)
admin.site.register(FoundItemRequest)
