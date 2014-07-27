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
        
    
    category = models.ForeignKey(Category,null=False, db_index = True)          
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    header = models.CharField(max_length=255,blank = False, null = False)
    tagline =  models.CharField(max_length=255,blank = False, null = False)
    search_words = models.CharField(max_length=255,blank = True, null = True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d', verbose_name = 'Thumbnail (320x180)')
    photos = models.ManyToManyField(Photo, null = True, blank = True)
    content = models.TextField(blank = False) 
    published = models.BooleanField(default=False, db_index=True)
    author = models.ForeignKey(User,null=True, blank=True)
    front_page = models.BooleanField(default=False, db_index=True)
    
    #This is so articles can be classified by category and sub category
    category_tags = models.ManyToManyField(Category, null =False, db_index = True, related_name = 'category_tags')
    
    def __unicode__(self):
        return self.name

        
    def save(self, *args, **kwargs):
        
        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())        
        super(Article, self).save(*args, **kwargs)
        
        #Need to save model first before adding category tags
        self.assign_category_tags()
   
    def assign_category_tags(self):
        category_tag = self.category
        while category_tag != None:
            self.category_tags.add(category_tag)
            category_tag = category_tag.parent
            
        
       
    