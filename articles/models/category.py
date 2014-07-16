from django.db import models
from articles.models.model_base import CoreModelBase

#Allows categories and sub categories
class Category(CoreModelBase):
    
    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'
        ordering =  ['path_and_name',]
        verbose_name_plural = "Categories"
        
    
    name = models.CharField(max_length=50, db_index=True, null = False, blank = False)
    parent = models.ForeignKey('self', blank = True, null = True, related_name="children")
    
    #Used for ordering within admin
    path_and_name = models.TextField()
    
    def __unicode__(self):
        return self.path_and_name

        
    #Creates path on save
    def save(self, *args, **kwargs):

        if self.parent is None:
            self.path_and_name = self.name
        else:
            self.path_and_name = self.parent.path_and_name + '\\' + self.name
            
        super(Category, self).save(*args, **kwargs)
    