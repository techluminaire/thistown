from django.contrib import admin
from articles.models.photo import Photo
       
class PhotoAdmin(admin.ModelAdmin):
    '''
    Photo admin customisation
    '''

    fieldsets = [
              (None,                {'fields': ['id','title','caption','image','photographer']}), 
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','title','caption', 'last_updated_date','creation_date','photographer')
    search_fields = ['title','caption','photographer']
    list_filter = ['photographer','creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')

#Registering models
admin.site.register(Photo,PhotoAdmin)

