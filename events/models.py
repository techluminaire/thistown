from django.db import models
from articles.models import Photo

# Create your models here.
class Event(models.Model):
    
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    start_datetime = models.DateTimeField(blank = False, db_index = True, null = False)
    photos = models.ManyToManyField(Photo, null = True, blank = True)
    content = models.TextField(blank = True) 
    published = models.BooleanField(default=False, db_index=True)
    youtube_embed = models.CharField(max_length=255,blank = True) 

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    
    
    def save(self, *args, **kwargs):
        
        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())        
        super(Event, self).save(*args, **kwargs)