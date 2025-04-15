from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('catalog/', views.catalog, name='catalog'),
    path('news/', views.news, name='news'),
    path('contacts/', views.contacts, name='contacts'),
    path('success_feedback/', views.success_feedback, name='success_feedback'),
    path('failure_feedback/', views.failure_feedback, name="failure_feedback"),
    path('page_not_found/', views.page_not_found, name="page_not_found"),
    path('catalog/service/<int:id>/', views.service_page, name="service"),
    path('catalog/service/success/', views.service_success, name="service_success"),
    path('documents/', views.documents, name="documents"),
    path('administrator/', views.admin_index, name="adminpanel_index"),
    path('administrator/auth/', views.admin_login, name="admin_login"),
    path('administrator/logout/', views.admin_logout, name='logout'),
    path('administrator/works/', views.admin_works, name="admin_works"),
    path('administrator/catalog/', views.admin_catalog, name="admin_catalog"),
    path('administrator/news/', views.admin_news, name="admin_news"),
    path('administrator/documents/', views.admin_documents, name="admin_documents"),
    path('administrator/reviews/', views.admin_reviews, name="admin_reviews"),
    path('administrator/db/catalog', views.admin_db_catalog, name="admin_db_catalog"),
    path('administrator/db/documents', views.admin_db_documents, name='admin_db_documents'),
    path('administrator/db/news', views.admin_db_news, name="admin_db_news"),
    path('administrator/db/reviews', views.admin_db_reviews, name="admin_db_reviews"),
    path('administrator/db/system_feedback', views.admin_db_system_feedback, name="admin_db_system_feedback"),
    path('administrator/db/system_tg', views.admin_db_system_tg, name="admin_db_system_tg"),
    path('administrator/db/works', views.admin_db_works, name="admin_db_works"),
]