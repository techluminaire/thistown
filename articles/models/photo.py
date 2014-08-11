from django.db import models


class Photo(models.Model):
    title = models.CharField(blank=False, max_length=255, db_index = True)
    caption = models.CharField(blank=True, max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Image 16:9 ratio')
    photographer = models.CharField(blank=True, max_length=255)
    
    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return self.title

    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'

