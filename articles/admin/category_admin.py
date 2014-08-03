from django.contrib import admin
from articles.models.category import Category
from articles.admin.admin_site import admin_site

class CategoryAdmin(admin.ModelAdmin):
    '''
    Category admin customisation
    '''

    fieldsets = [
              (None,                {'fields': ['id','name','sequence','parent']}), 
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','name','path_and_name', 'last_updated_date','creation_date',)
    search_fields = ['name',]
    readonly_fields = ('last_updated_date','creation_date','id',)

#Registering models
admin_site.register(Category,CategoryAdmin)
