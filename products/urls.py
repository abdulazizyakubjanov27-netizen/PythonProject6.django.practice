from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
]