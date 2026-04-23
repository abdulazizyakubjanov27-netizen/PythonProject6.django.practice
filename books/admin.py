from django.contrib import admin
from .models import Book, Author

# admin.site.register(Books)
# admin.site.register(Author)

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')