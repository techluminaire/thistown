from django.contrib import admin
from articles.models.article import Article
#from Core.widgets import VerboseManyToManyRawIdWidget


class ArticleAdmin(admin.ModelAdmin):
    '''
    Article admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','name','category','search_words','published','front_page','header','tagline','photos','content','author']}), 
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ] 
    
    list_display = ('id','name','category', 'last_updated_date','creation_date','published','front_page')
    search_fields = ['search_words','name','header','tagline',]
    list_filter = ['category','front_page','creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')
    raw_id_fields = ('photos',)


    
    #Auto populates author field with current user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(ArticleAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
    
admin.site.register(Article, ArticleAdmin)