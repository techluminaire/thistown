from articles.models.model_base import CoreModelBase
from django.db import models


class Photo(CoreModelBase):
    title = models.CharField(blank=False, max_length=255, db_index = True)
    caption = models.CharField(blank=True, max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    photographer = models.CharField(blank=True, max_length=255)
    
    def __unicode__(self):
        return self.title

    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'