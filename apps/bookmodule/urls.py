from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_books, name='books.search'),
    path('', views.index, name='books.index'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('html5/links/', views.links, name='books.links'),
    path('html5/text/formatting/', views.formatting, name='books.formatting'),
    path('html5/listing/', views.listing, name='books.listing'),
    path('html5/tables/', views.tables, name='books.tables'),  # Add this line for tables page
    path('simple/query/', views.simple_query, name='simple_query'),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),
    path('lab8/task1/', views.task1, name='lab8_task1'),
    path('lab8/task2/', views.task2, name='lab8_task2'),
    path('lab8/task3/', views.task3, name='lab8_task3'),
    path('lab8/task4/', views.task4, name='lab8_task4'),
    path('lab8/task5/', views.task5, name='lab8_task5'),
    path('lab8/task6/', views.task6, name='lab8_task6'),
    path('lab8/task7/', views.task7, name='lab8_task7'),
]
