from .forms import *
from .models import *

def get_system_info(request):
    http = {
        'encoding' : request.META.get('HTTP_ACCEPT_ENCODING') if request.META.get('HTTP_ACCEPT_ENCODING') else "None",
        'host' : request.META.get('HTTP_HOST') if request.META.get('HTTP_HOST') else "None",
        'user_agent' : request.META.get('HTTP_USER_AGENT') if request.META.get('HTTP_USER_AGENT') else "None",
        'referer' : request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else "None",
        'ip' : request.META.get('REMOTE_ADDR') if request.META.get('REMOTE_ADDR') else "None",
        'user' : request.META.get('REMOTE_USER') if request.META.get('REMOTE_USER') else "None",
        'method' : request.META.get('REQUEST_METHOD') if request.META.get('REQUEST_METHOD') else "None",
        'server_name' : request.META.get('SERVER_NAME') if request.META.get('SERVER_NAME') else "None",
        'server_port' : request.META.get('SERVER_PORT') if request.META.get('SERVER_PORT') else "None",
        'server_host' : request.META.get('SERVER_HOST') if request.META.get('SERVER_HOST') else "None",
    }
    return http


def search_func(request):
    if request.method == "POST":
        search_query = request.POST.get('search', '')
        if search_query:
            works = Works.objects.filter(name__icontains=search_query)
            catalog = Catalog.objects.filter(name__icontains=search_query)
            news = News.objects.filter(title__icontains=search_query)
            documents = Documents.objects.filter(title__icontains=search_query)
            
            context = {
                "search_query": search_query,
                "works": works,
                "catalog": catalog,
                "news": news,
                "documents": documents
            }
            return context
    return None

