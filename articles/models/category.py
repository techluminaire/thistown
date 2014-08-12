from django.db import models


class Category(models.Model):
    '''
    Allows classification of articles.  Also used to build top menu
    Allows categories and sub categories
    '''
    
    class Meta:
        '''
        This is to allow models to be spread across multiple files
        '''
        app_label = 'articles'
        ordering =  ['path_and_name',]
        verbose_name_plural = "Categories"
        
    
    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False)
    sequence = models.IntegerField(null=True, db_index=True)
    parent = models.ForeignKey('self', blank = True, null = True, related_name="children", db_index=True)
    
    #Used for ordering within admin
    path_and_name = models.TextField()
    
    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True) 
    
    def __unicode__(self):
        return self.path_and_name

        
    #Creates path on save
    def save(self, *args, **kwargs):

        if self.parent is None:
            self.path_and_name = self.name
        else:
            self.path_and_name = self.parent.path_and_name + '/' + self.name
            
        super(Category, self).save(*args, **kwargs)
    