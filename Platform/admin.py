from django.contrib import admin
import Platform
# Register your models here.
class PlatformModelAdmin(admin.ModelAdmin):
    list_display = ('bbdid','appuuid')


admin.site.register(Platform,PlatformModelAdmin)