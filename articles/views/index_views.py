#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Category
   
def index(request):
    
    #Get the top level categories
    template = loader.get_template('articles/index.html')
    context = RequestContext(request,{
                                      'categories': Category.objects.filter(parent = None).order_by('sequence')                                  
                                      })
    response = template.render(context)
    return HttpResponse(response)  


def category_index(request,category_name):

    template = loader.get_template('articles/category_index.html')
    context = RequestContext(request,{
                                      'sub_category_name': category_name,
                                      'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                      'category_name': category_name,
                                      'sub_categories': Category.objects.filter(parent__name = category_name).order_by('sequence')                                  
                                      })
    response = template.render(context)
    return HttpResponse(response)  

 
def sub_category_index(request,category_name,sub_category_name):
    
    template = loader.get_template('articles/category_index.html')
    context = RequestContext(request,{
                                      'sub_category_name': sub_category_name,
                                      'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                      'category_name': category_name,
                                      'sub_categories': Category.objects.filter(parent__name = category_name).order_by('sequence')                                  
                                      })
    response = template.render(context)
    return HttpResponse(response)    