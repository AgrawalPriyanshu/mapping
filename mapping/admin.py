from django.contrib import admin
from .models import Game,Athlete,Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display=('registration_id','registration_date',)
    filter_horizontal = ('game_name',)
    search_fields=('registration_id',)
    list_filter=('registration_date',)
    date_hierarchy='registration_date'

class AthleteAdmin(admin.ModelAdmin):
    ordering=('-athlete_name',)
# Register your models here.
admin.site.register(Game)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Registration, RegistrationAdmin)
