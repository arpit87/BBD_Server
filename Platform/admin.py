from django.contrib import admin
from Platform.models import APPDATA
# Register your models here.
class PlatformModelAdmin(admin.ModelAdmin):
    list_display = ('bbdid','appuuid')


admin.site.register(APPDATA,PlatformModelAdmin)