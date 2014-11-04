# Register your models here.
from django.contrib import admin
from Beep.models import Beep,SentBeep

class BeepsModelAdmin(admin.ModelAdmin):
    list_display = ('beepid','beep_str','beeplevel','created_by')

class SendBeepModelAdmin(admin.ModelAdmin):
    list_display = ('beepid', 'from_id', 'to_id', 'date_time')


admin.site.register(Beep,BeepsModelAdmin)
admin.site.register(SentBeep,SendBeepModelAdmin)
