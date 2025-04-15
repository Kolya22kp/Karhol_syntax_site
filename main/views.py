from datetime import tzinfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from time import tzname
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import *
from .forms import *
import requests
from urllib.parse import quote
from .auxiliary_func import *
import logging
from django.utils.timezone import localtime
from datetime import datetime


def home(request):
    response = Reviews.objects.all()
    context = {
        "Reviews": response
    }
    if request.method == "GET":
        return render(request, 'index.html', context=context)
    elif request.method == "POST":
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
            return render(request, 'search_results.html', context=context)

        return redirect('/')
    
def search_result(request):
    pass

def works(request):
    response = Works.objects.all()
    context = {
        "Works": response
    }
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    
    return render(request, 'works.html', context=context)

def catalog(request):
    response = Catalog.objects.all()
    context = {
        "goods": response
    }
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    return render(request, 'catalog.html', context=context)

def news(request):
    response = News.objects.all()
    context = {
        "news": response
    }
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    for item in context["news"]:
        print(item.description)
    return render(request, 'news.html', context=context)

def contacts(request):
    if request.method == "GET":
        context = {
            "form": FeedbackForm()
        }
        return render(request, 'contacts.html', context=context)
    else:
        sc = search_func(request)
        if sc:
           return render(request, 'search_results.html', context=sc)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            token = '7853451283:AAHMogrNdjOWaTS8pBau5piXF7Nu83Vl5pM'
            chat_id = '-4772837381'
            text = f"📩 Новое сообщение!\n\n👤 Клиент: {form.data['name']}\n📫 Почта: {form.data['email']}\n🔗 Контакт: {form.data['login']}\n📃 Сообщение:\n{form.data['text']}"            
            data = get_system_info(request)
            system_text = (
                f"\n---------------\nИнформация о пользователе\nIP: {data["ip"]}\n"
                f"User agent: {data["user_agent"]}\n"
                f"From page: {data["referer"]}\n"
                f"Host name: {data["host"]}\n"
                f"Server: {data["server_name"]} {data["server_port"]} {data["server_host"]}\n"
            )
            system_text = (
                system_text
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("&", "&amp;")
                .replace("built-in", "code")
            )
            encoded_message = quote(text + system_text)
            sendToTelegram = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={encoded_message}"
            status = requests.get(sendToTelegram).json()

            conn = System_contacts(name = form.data["name"], email = form.data["email"], login = form.data["login"], message = form.data["text"])
            conn.system = (
                f"ip: {data['ip']} |"
                f" user: {data['user']} |"
                f" user_agent: {data['user_agent']} |"
                f" host: {data['host']} |"
                f" method: {data['method']} |"
                f" referer: {data['referer']} |"
                f" encoding: {data['encoding']} |"
                f" server: {data['server_name']} {data['server_port']} {data['server_host']}"
            )
            conn.save()


            if status:
                return redirect("/success_feedback/")
            return redirect("/failure_feedback/")
    

def success_feedback(request):
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    return render(request, 'success_feedback.html')

def failure_feedback(request):
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    return render(request, 'failure_feedback.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def service_page(request, id):
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    response = Catalog.objects.get(id=id)
    print(response)
    context = {
        "service": {
        "name": response.name,
        "image": "",
        "price": response.price,
        "old_price": response.old_price,
        "estimated_time": response.estimated_time,
        "description": response.description,
        "requirements": "Четкое техническое задание с детальным описанием целей проекта, конкретными функциональными требованиями, информацией о целевой аудитории и платформах/устройствах для использования; полный комплект необходимых материалов (логотипы, изображения, текстовый контент, шрифты, API ключи, базы данных или любые другие данные для интеграции); информацию о текущих системах, если проект связан с уже существующими решениями; готовность предоставлять оперативную обратную связь на каждом этапе разработки, включая тестирование и утверждение результатов; четкое указание приоритетов задач и возможных ограничений (временных, технических или других).",
        "cancellation_terms": "Мы можем отказать в сотрудничестве при отсутствии четкого ТЗ, неопределенности бюджета, нереалистичных сроках, нарушении условий оплаты, использовании материалов с нарушением авторских прав, presence в проектах с противозаконной деятельностью или высоким уровнем рисков.",
        "booking_terms": "Все условия фиксируются в официальном договоре, включая этапы оплаты (предоплата 40-60%, промежуточные платежи и финальный расчет), согласованные сроки выполнения, ограниченный период технической поддержки после сдачи проекта, передачу прав на результат после полной оплаты и возможность использования проекта в портфолио студии"
    
        }
    }
    
    return render(request, 'service.html', context=context)


def service_success(request):
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    data = get_system_info(request)
    logging.info("Get data for http-request")
    conn = System_redirects_tg(ip = data["ip"], user_agent = data["user_agent"], referer = data["referer"], host = data["host"], method = data["method"], server_name = data["server_name"], server_port = data["server_port"], server_host = data["server_host"], date = localtime().ctime())
    conn.save()
    if conn:
        logging.info("Model save success")
    return render(request, 'service_success.html')


def documents(request):
    sc = search_func(request)
    if sc:
        return render(request, 'search_results.html', context=sc)
    context = {
        "docs": Documents.objects.all()
    }
    return render(request, 'documents.html', context=context)


#ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN


@login_required
def admin_index(request):
    return render(request, "adminpanel/index.html")

def admin_login(request):
    if request.user.is_authenticated:
        redirect('/administrator/')
    context = {
            "form": LoginForm()
        }
    if request.method == "GET":
        return render(request, "adminpanel/auth.html", context=context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data["username"], password=form.data["password"])
            if user is not None:
                login(request, user)
            if request.user.is_authenticated:
                return redirect('/administrator/')
            else:
                context["errors"] = "Уважаемый пользователь, в процессе выполнения процедуры авторизации возникла ошибка, препятствующая успешной идентификации."
                return render(request, "adminpanel/auth.html", context=context)
            

def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/administrator/')
    

@login_required(login_url="/administrator/auth")
def admin_works(request):
    context = {
        "form": ManagementWorksForm()
    }
    if request.method == "GET":
        return render(request, "adminpanel/management/works.html", context=context)
    form = ManagementWorksForm(request.POST)
    if form.is_valid():
        conn = Works(name=form.data["name"], image=form.data["image"])
        conn.save()
        return redirect("/administrator/")
    
@login_required(login_url="/administrator/auth")
def admin_catalog(request):
    context = {
        "form": ManagementCatalogForm()
    }
    if request.method == "GET":
        return render(request, "adminpanel/management/catalog.html", context=context)
    form = ManagementCatalogForm(request.POST)
    if form.is_valid():
        conn = Catalog(name=form.data["name"], price=form.data["price"], old_price = form.data["old_price"], estimated_time=form.data["estimated_time"], description=form.data["description"])
        conn.save()
        return redirect("/administrator/")

@login_required(login_url="/administrator/auth")
def admin_news(request):
    context = {
        "form": ManagementNewsForm()
    }
    if request.method == "GET":
        return render(request, "adminpanel/management/news.html", context=context)
    form = ManagementNewsForm(request.POST)
    if form.is_valid():
        now = datetime.now()
        date = now.strftime("%d.%m.%Y %H:%M:%S")
        conn = News(title=form.data["title"], date=date, description=form.data["description"])
        conn.save()
        return redirect("/administrator/")

@login_required(login_url="/administrator/auth")
def admin_documents(request):
    context = {
        "form": ManagementDocumentsForm()
    }
    if request.method == "GET":
        return render(request, "adminpanel/management/documents.html", context=context)
    form = ManagementDocumentsForm(request.POST)
    if form.is_valid():
        if Documents.objects.filter(name=form.data["name"]) != None:
            context["errors"] = ["Ошибка, данное имя документа (системное) уже занято, измените его."]
            return render(request, "adminpanel/management/documents.html", context=context)
        conn = Documents(name=form.data["name"], title=form.data["title"], content=form.data["content"])
        conn.save()
        return redirect("/administrator/")

@login_required(login_url="/administrator/auth")
def admin_reviews(request):
    context = {
        "form": ManagementReviewsForm()
    }
    if request.method == "GET":
        return render(request, "adminpanel/management/reviews.html", context=context)
    form = ManagementReviewsForm(request.POST)
    if form.is_valid():
        conn = Reviews(name=form.data["name"], estimation=form.data["estimation"], description=form.data["description"])
        conn.save()
        return redirect("/administrator/")
    



#ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB ADMIN DB

@login_required(login_url="/administrator/auth")
def admin_db_catalog(request):
    context = {
        "catalog": Catalog.objects.all()
    }
    return render(request, "adminpanel/database/catalog.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_documents(request):
    context = {
        "documents": Documents.objects.all()
    }
    return render(request, "adminpanel/database/documents.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_news(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "adminpanel/database/news.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_reviews(request):
    context = {
        "reviews": Reviews.objects.all()
    }
    return render(request, "adminpanel/database/reviews.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_system_feedback(request):
    context = {
        "system_feedback": System_contacts.objects.all()
    }
    return render(request, "adminpanel/database/system_feedback.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_system_tg(request):
    context = {
        "system_tg": System_redirects_tg.objects.all()
    }
    return render(request, "adminpanel/database/system_tg.html", context=context)

@login_required(login_url="/administrator/auth")
def admin_db_works(request):
    context = {
        "works": Works.objects.all()
    }
    return render(request, "adminpanel/database/works.html", context=context)