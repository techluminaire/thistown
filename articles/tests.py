from django.test import TestCase
from articles.models import Category
from articles.models import Article
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
        
    def test_update_front_page_records_deletes_existing_front_page_records(self):
        parent = Category.objects.create(name = 'parent1', sequence = 1, parent = None)
        parent.save()   
#     