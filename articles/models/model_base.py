from django.db import models


class CoreModelBase(models.Model):
    '''
    Base model for all entity elements
    '''
    
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    
    class Meta:
        '''
        This is to allow models spread across multiple files
        '''
        abstract = True
        app_label = 'articles' 
          
             
    def save(self, *args, **kwargs):
        super(CoreModelBase, self).save(*args, **kwargs)
        