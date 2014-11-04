# Register your models here.
from django.contrib import admin
from User.models import UserDetails,Friend

class UserDetailsModelAdmin(admin.ModelAdmin):
    list_display = ('bbdid','name','date_joined')

class FriendModelAdmin(admin.ModelAdmin):
    list_display = ('bbdid','friend_bbd_id')


admin.site.register(UserDetails,UserDetailsModelAdmin)
admin.site.register(Friend,FriendModelAdmin)
