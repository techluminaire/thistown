from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from articles.models import Article,Category

   
def search_results(request, search_text):
    
    try:        
        page_template = 'articles/search_results_page.html'
                
        if request.is_ajax(): #Getting results
            context = {
                       'articles': Article.objects.filter(published = True, search_words__contains = search_text).order_by('-creation_date'),
                       'page_template': page_template,
                       }
            template = 'articles/search_results_page.html'
            
        else: #Getting full page
            
            if Article.objects.filter(published = True, search_words__contains = search_text).count() > 0:
                context = {
                          'categories': Category.objects.filter(parent = None).order_by('sequence'),
                          'articles': Article.objects.filter(published = True, search_words__contains = search_text).order_by('-creation_date'),
                          'page_template': page_template,                                  
                          }
                template = 'articles/search_results.html'
            
            else: #No results
                context = {
                          'categories': Category.objects.filter(parent = None).order_by('sequence'),                                 
                          }
                template = 'articles/search_no_results.html'
                
        return render_to_response(
                template, context, context_instance=RequestContext(request))
 
        
    except: #page not found for any errors
        
        template = loader.get_template('articles/page_not_found.html')
        context = RequestContext(request,{
                                          'categories': Category.objects.filter(parent = None).order_by('sequence'),                     
                                          })
     
        response = template.render(context)
        return HttpResponse(response)
 
