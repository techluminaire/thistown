from django.test import TestCase
from articles.models import Category
from articles.models import Article
from articles.models import Photo
from articles.models import FrontPageArticle
import os


#All the tests for the Category model
class CategoryTests(TestCase):
           
    
    def test_path_and_name_assigned_parent_category(self):
        category = Category.objects.create(name = 'example', sequence = 1, parent = None)
        category.save()
         
        self.assertEqual(category.path_and_name, 'example')
 
    def test_path_and_name_assigned_subcategory(self):
        parent_category = Category.objects.create(name = 'parent', sequence = 1, parent = None)
        parent_category.save()
         
        sub_category = Category.objects.create(name = 'sub', sequence = 1, parent = parent_category)
        sub_category.save()
        self.assertEqual(sub_category.path_and_name, 'parent/sub')
        
#Tests for he article model
class ArticleTests(TestCase):
     
    def setUp(self):      
        self.TEST_DIR =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_data')
         
     
    def test_assign_category_tags_parent_category(self):
        category = Category.objects.create(name = 'category1', sequence = 1, parent = None)
        category.save()
         
        article = Article.objects.create(
                                category = category
                                ,name = 'article1'
                                ,header = 'header'
                                ,tagline = 'tagline'
                                ,thumbnail =  os.path.join(self.TEST_DIR, 'test_image.jpg')
                                ,content = '<p>test</p>'
                                )
         
        article.save()
         
        self.assertIn(category, article.category_tags.all())
        
        
        
    def test_assign_category_tags_sub_category(self):
        parent = Category.objects.create(name = 'parent1', sequence = 1, parent = None)
        parent.save()
        
        sub = Category.objects.create(name = 'sub1', sequence = 1, parent = parent)
        sub.save()
         
        article = Article.objects.create(
                                category = sub
                                ,name = 'article1'
                                ,header = 'header'
                                ,tagline = 'tagline'
                                ,thumbnail =  os.path.join(self.TEST_DIR, 'test_image.jpg')
                                ,content = '<p>test</p>'
                                )
         
        article.save()
                                           
        self.assertIn(sub, article.category_tags.all())
        self.assertIn(parent, article.category_tags.all())
        
    def test_update_front_page_records_creates_and_updates_new_front_page_records(self):
        category = Category.objects.create(name = 'cat1', sequence = 1, parent = None)
        category.save()   
        
        article = Article.objects.create(
                                category = category
                                ,name = 'name'
                                ,header = 'header'
                                ,tagline = 'tagline'
                                ,thumbnail =  os.path.join(self.TEST_DIR, 'test_image.jpg')
                                ,content = '<p>test</p>'
                                ,front_page = True
                                )
         
        article.save()
        
        photo = Photo.objects.create(title = 'title',caption = 'caption', image = os.path.join(self.TEST_DIR, 'test_image.jpg'), photographer = 'photographer')
        photo.save()
        article.photos.add(photo.id)
        
        self.assertEqual(1, FrontPageArticle.objects.filter(article__id = article.id).count())
        front_page_article = FrontPageArticle.objects.filter(article__id = article.id)[0]
        self.assertEqual(front_page_article.article_name, 'name')
        self.assertEqual(front_page_article.image, os.path.join(self.TEST_DIR, 'test_image.jpg'))
        self.assertEqual(front_page_article.creation_date, article.creation_date)
        
        #Check if there is no photo, it is not on front page
        article.photos.remove(photo.id)
        self.assertEqual(0, FrontPageArticle.objects.filter(article__id = article.id).count())
        
        #Check if we put photo back it is on front page
        article.photos.add(photo.id)
        self.assertEqual(1, FrontPageArticle.objects.filter(article__id = article.id).count())
        
        #Check if we untick 'front_page', it is removed from front page
        article.front_page = False
        article.save()
        self.assertEqual(0, FrontPageArticle.objects.filter(article__id = article.id).count())
    