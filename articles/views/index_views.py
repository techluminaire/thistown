from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Category, Article, FrontPageArticle


   
def index(request):
    
    #Get the top level categories
    template = loader.get_template('articles/index.html')
    context = RequestContext(request,{
                                      'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                      'articles': FrontPageArticle.objects.all().order_by('creation_date'),                                  
                                      })
    response = template.render(context)
    return HttpResponse(response)  


def category_index(request,category_name):

    template = 'articles/category_index.html'
    page_template = 'articles/category_index_page.html'
    
    
    if request.is_ajax():
        context = {
                   'entries': Article.objects.filter(published = True, category_tags__name = category_name).order_by('creation_date'),
                   'page_template': page_template,
                   }
        template = page_template
    else:
        context = {
                  'sub_category_name': category_name,
                  'categories': Category.objects.filter(parent = None).order_by('sequence'),
                  'category_name': category_name,
                  'sub_categories': Category.objects.filter(parent__name = category_name).order_by('sequence'),
                  'entries': Article.objects.filter(published = True, category_tags__name = category_name).order_by('creation_date'),
                  'page_template': page_template,                                  
                  }
    

    return render_to_response(
            template, context, context_instance=RequestContext(request))


 
def sub_category_index(request,category_name,sub_category_name):
    
    template = 'articles/category_index.html'
    page_template = 'articles/category_index_page.html'

    if request.is_ajax():
        context = {
                   'entries': Article.objects.filter(published = True, category_tags__name = sub_category_name).order_by('creation_date'),
                   'page_template': page_template,
                   }
        template = page_template
    else:    
        context = {
                  'sub_category_name': category_name,
                  'categories': Category.objects.filter(parent = None).order_by('sequence'),
                  'category_name': category_name,
                  'sub_categories': Category.objects.filter(parent__name = category_name).order_by('sequence'),
                  'entries': Article.objects.filter(published = True, category_tags__name = sub_category_name).order_by('creation_date'),
                  'page_template': page_template,                                  
                  }
    

    return render_to_response(
            template, context, context_instance=RequestContext(request))

