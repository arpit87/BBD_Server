from django.contrib import admin
from Trends.models import beeptimetrends,individualbeeptrends

class BeepTimeTrendsModelAdmin(admin.ModelAdmin):
    list_display = ('beep_id','beep_freq','trend_type')

class IndividualTimeTrendsModelAdmin(admin.ModelAdmin):
    list_display = ('beep_id','beep_freq','trend_type')


admin.site.register(beeptimetrends,BeepTimeTrendsModelAdmin)
admin.site.register(individualbeeptrends,IndividualTimeTrendsModelAdmin)
