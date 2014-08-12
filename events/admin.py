from django.contrib import admin
from events.models import CalendarEvent,Venue
from django.db import models
from django.forms import TextInput, Textarea
from articles.admin.admin_site import admin_site



class CalendarEventAdmin(admin.ModelAdmin):
    '''
    Event admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','name','venue','start_datetime','published','heading','photos','content']}), 
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','name','venue','start_datetime','published')
    search_fields = ['name','heading',]
    list_filter = ['venue','start_datetime','creation_date']
    readonly_fields = ('last_updated_date','creation_date','id')
    raw_id_fields = ('venue','photos',)


    
admin_site.register(CalendarEvent, CalendarEventAdmin)

class VenueAdmin(admin.ModelAdmin):
    '''
    Venue admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','name']}), 
              ('Location',  {'fields':['address1','address2','town_or_city','postcode','maps_embed']}),
              ('Contact',  {'fields':['website','email','telephone_number']}),
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','name', 'town_or_city','postcode')
    search_fields = ['name',]
    list_filter = ['creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':15, 'cols':100})},
    }

admin_site.register(Venue,VenueAdmin)