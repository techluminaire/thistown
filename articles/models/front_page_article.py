from django.db import models
from articles.models.article import Article 

#This objects of this model are auto created and provide a quick lookup of front page articles

class FrontPageArticle(models.Model):
    
    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'
        
    article = models.ForeignKey(Article, null = False, blank = False, unique = True)
    article_name = models.CharField(max_length=255, unique=True, blank = False, null = False)
    tagline =  models.CharField(max_length=255,blank = False, null = False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null = False)
    creation_date = models.DateTimeField(db_index=True)