from django.urls import path
from . import views

app_name = 'doc_processor'

urlpatterns = [
    path('', views.process_document, name='upload'),
       path('description/<int:keyword_id>/', views.keyword_description, name='description'),
     
]
