from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Category
from articles.models import Article


def article_view(request,article_name):
    
    #Get the article by name
    try:
        article = Article.objects.get(name=article_name)
        template = loader.get_template('articles/article.html')
        context = RequestContext(request,{
                                          'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                          'article': article,
                                          'photos': article.photos.all()                              
                                          })
        
    #article not found show a not found
    except Article.DoesNotExist:
        template = loader.get_template('articles/article_not_found.html')
        context = RequestContext(request,{
                                          'categories': Category.objects.filter(parent = None).order_by('sequence'),                     
                                          })
     
    response = template.render(context)
    return HttpResponse(response)  