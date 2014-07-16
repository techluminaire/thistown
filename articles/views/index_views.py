#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

   
def index(request):
    
    template = loader.get_template('articles/index.html')
    context = RequestContext(request)
    response = template.render(context)
    return HttpResponse(response)  
