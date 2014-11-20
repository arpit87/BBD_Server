from django.contrib import admin
from Trends.models import beeptimetrends,individualbeeptrends,TrendsUpdateLastTime

class BeepTimeTrendsModelAdmin(admin.ModelAdmin):
    list_display = ('beep','beep_freq','is_new','trend_type')

class IndividualTimeTrendsModelAdmin(admin.ModelAdmin):
    list_display = ('bbs_id','beep_freq','trend_type')

class TrendsLastUpdateTimeModelAdmin(admin.ModelAdmin):
    list_display = ('trend_type','last_update_time')

admin.site.register(beeptimetrends,BeepTimeTrendsModelAdmin)
admin.site.register(individualbeeptrends,IndividualTimeTrendsModelAdmin)
admin.site.register(TrendsUpdateLastTime,TrendsLastUpdateTimeModelAdmin)
