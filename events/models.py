from django.db import models
from articles.models import Photo


class Venue(models.Model):
    '''
    Represents the venue for an event
    '''
    
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    
    #Location
    address1 = models.CharField(max_length=255,blank = False, null = False, verbose_name = 'Address Line 1')
    address2 = models.CharField(max_length=255,blank = True, null = True, verbose_name = 'Address Line 2')
    town_or_city = models.CharField(max_length=60,blank = False, null = False, verbose_name = 'Town/City')
    postcode = models.CharField(max_length=8,blank = False, null = False)
    
    maps_embed = models.TextField(blank = True)
    
    #Contact details
    website = models.CharField(max_length=255,blank = True, null = True)
    email = models.CharField(max_length=255,blank = True, null = True)
    telephone_number = models.CharField(max_length=20,blank = True, null = True)
    
    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return self.name

class CalendarEvent(models.Model):
    '''
    Represents an event that will take place
    '''
    
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    heading = models.CharField(max_length=255,blank = False, null = False)
    
    venue = models.ForeignKey(Venue, null = False, db_index = True) 
    start_datetime = models.DateTimeField(blank = False, db_index = True, null = False, verbose_name = 'Start Date & Time')
    
    photos = models.ManyToManyField(Photo, null = True, blank = True)
    content = models.TextField(blank = True) 
    published = models.BooleanField(default=False, db_index=True)
       

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())        
        super(CalendarEvent, self).save(*args, **kwargs)



    