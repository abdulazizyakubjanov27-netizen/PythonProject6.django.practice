from django.urls import path
from . import views

# 1-page url -> view -> template(html)
# urlpatterns = [
#     path('list/', views.book_list, name='book_list'),
#     path('detail/<int:pk>/', views.book_detail, name='book_detail'),
#     path('create-form/', views.book_create_form, name='book_create_form'),
#     path('create/', views.book_create, name='book_create'),
#     path('update-form/<int:pk>/', views.book_update_forme, name='book_update_form'),
#     path('update/<int:pk>/', views.book_update, name='book_update'),
#     path('delete/<int:pk>/', views.book_delete, name='book_delete'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/edit/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]



