from articles.models.model_base import CoreModelBase
from django.db import models
from articles.models.category import Category 
from articles.models.photo import Photo
from django.contrib.auth.models import User

#Represents an article
class Article(CoreModelBase):
    
    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'
        
    
    category = models.ForeignKey(Category,null=False, db_index=True)          
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    header = models.CharField(max_length=255,blank = False, null = False)
    tagline =  models.CharField(max_length=255,blank = False, null = False)
    search_words = models.CharField(max_length=255,blank = True, null = True)
    photos = models.ManyToManyField(Photo, null = True, blank = True)
    content = models.TextField(blank = False) 
    published = models.BooleanField(default=False, db_index=True)
    author = models.ForeignKey(User,null=False, blank=True)
    front_page = models.BooleanField(default=False, db_index=True)
    
    def __unicode__(self):
        return self.name


   
   
    