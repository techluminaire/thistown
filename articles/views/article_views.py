from django.http import HttpResponse
from django.template import RequestContext, loader
from articles.models import Category
from articles.models import Article
from thistown import settings

def article_view(request,article_name):
    
    #Get the article by name
    try:
        article = Article.objects.get(name=article_name)
        template = loader.get_template('articles/article.html')
        context = RequestContext(request,{
                                          'categories': Category.objects.filter(parent = None).order_by('sequence'),
                                          'article': article,
                                          'photos': article.photos.all(),  
                                          'absolute_uri':  settings.HOST_DOMAIN + request.get_full_path(),                         
                                          })
        
    #article not found show a not found
    except:
        from articles.views import page_not_found
        return page_not_found(request)
     
    response = template.render(context)
    return HttpResponse(response)  