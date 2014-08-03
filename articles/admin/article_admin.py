from django.contrib import admin
from articles.models.article import Article
from django.db import models
from django.forms import TextInput, Textarea
from articles.admin.admin_site import admin_site



class ArticleAdmin(admin.ModelAdmin):
    '''
    Article admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','name','category','search_words','published','front_page','header','tagline','thumbnail','photos','content','author']}), 
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','name','category', 'last_updated_date','creation_date','published','front_page')
    search_fields = ['search_words','name','header','tagline',]
    list_filter = ['category','front_page','creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')
    raw_id_fields = ('photos',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':50, 'cols':100})},
    }
    
    #Auto populates author field with current user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(ArticleAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
    
admin_site.register(Article, ArticleAdmin)