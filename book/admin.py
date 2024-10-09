from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')  
    ordering = ('published_date',)  
    
admin.site.register(BookAdmin)
