from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Category, Article, FrontPageArticle
from articles.common import custom_strftime


def page_not_found(request): 
    #Default page not found view
    template = loader.get_template('articles/page_not_found.html')
    context = RequestContext(request,{
                                      'categories': Category.objects.filter(parent = None).order_by('sequence'),                     
                                      }) 
    response = template.render(context)
    return HttpResponse(response)  

def index(request):
    import datetime
    d = datetime.datetime.now()
    
    #Get the top level categories
    template = loader.get_template('articles/index.html')
    context = RequestContext(request,{
                                      'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                      'articles': FrontPageArticle.objects.all().order_by('creation_date'),
                                      'day': custom_strftime("{S}",d),
                                      'day_of_week': d.strftime("%A"),
                                      'month': d.strftime("%B"),                                                                        
                                      })
    
    response = template.render(context)
    return HttpResponse(response)  


def category_index(request,category_name):

    template = 'articles/category_index.html'
    page_template = 'articles/category_index_page.html'
    
    try:
        category =  Category.objects.get(name = category_name)
    except Category.DoesNotExist:
        return page_not_found(request)
        
    
    if request.is_ajax():
        context = {
                   'entries': Article.objects.filter(published = True, category_tags__id = category.id).order_by('-creation_date'),
                   'page_template': page_template,
                   }
        template = page_template
    else:
        context = {
                  'sub_category_name': category.name,
                  'categories': Category.objects.filter(parent = None).order_by('sequence'),
                  'category_name': category.name,
                  'sub_categories': Category.objects.filter(parent__id = category.id).order_by('sequence'),
                  'entries': Article.objects.filter(published = True, category_tags__id = category.id).order_by('-creation_date'),
                  'page_template': page_template,                                  
                  }
    

    return render_to_response(
            template, context, context_instance=RequestContext(request))


 
def sub_category_index(request,category_name,sub_category_name):
    
    template = 'articles/category_index.html'
    page_template = 'articles/category_index_page.html'

    try:
        category =  Category.objects.get(name = category_name)
    except Category.DoesNotExist:
        return page_not_found(request) 
    
    try:
        sub_category =  Category.objects.get(name = sub_category_name)
    except Category.DoesNotExist:
        return page_not_found(request) 

    if request.is_ajax():
        context = {
                   'entries': Article.objects.filter(published = True, category_tags__name = sub_category_name).order_by('creation_date'),
                   'page_template': page_template,
                   }
        template = page_template
    else:    
        context = {
                  'sub_category_name': sub_category.name,
                  'categories': Category.objects.filter(parent = None).order_by('sequence'),
                  'category_name': category.name,
                  'sub_categories': Category.objects.filter(parent__id = category.id).order_by('sequence'),
                  'entries': Article.objects.filter(published = True, category_tags__id = sub_category.id).order_by('creation_date'),
                  'page_template': page_template,                                  
                  }
    

    return render_to_response(
            template, context, context_instance=RequestContext(request))

