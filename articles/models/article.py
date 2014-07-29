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

    def __init__(self, *args, **kwargs):
        '''
        Initialization of object
        Keeps track of original values in initialization
        '''
        super(Article, self).__init__(*args, **kwargs)
        
        self._original_front_page = self.front_page

    
        
    def save(self, *args, **kwargs):
        
        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())        
        super(Article, self).save(*args, **kwargs)
        
        #Need to save model first before adding category tags
        self.assign_category_tags()
        
        self.update_front_page_records()
   
   
    def assign_category_tags(self):
        '''
        Creates faster lookup tags to filter by category and parent category
        '''
        
        category_tag = self.category
        while category_tag != None:
            self.category_tags.add(category_tag)
            category_tag = category_tag.parent
            
        
    def update_front_page_records(self):   
        '''
        Creates fast lookup data to be displayed on the front page
        '''
        
        from articles.models.front_page_article import FrontPageArticle
        
        #Remove any front page record associated with article  
        try:
            FrontPageArticle.objects.filter(article__id=self.id).delete()
        except:
            pass
        
        #Article not longer on front page or does not have a photo, so finish
        if not self.front_page or self.photos.count() == 0:         
            return
        
        #Article is on front page so add record
        FrontPageArticle.objects.create(article = self
                                        ,article_name = self.name
                                        ,tagline = self.tagline
                                        ,image = self.photos.all()[0].image
                                        ,creation_date = self.creation_date)
    