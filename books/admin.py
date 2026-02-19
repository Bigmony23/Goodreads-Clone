from django.contrib import admin
from .models import Book,Book_Author ,Book_Review,Author

class BookAdmin(admin.ModelAdmin):
    list_display=('title','description','isbn')
    search_fields=['title']
    list_filter=['isbn','id','title']

class Book_AuthorAdmin(admin.ModelAdmin):
    list_display=('book','author')
    filter=('author','id','book')
class Book_ReviewAdmin(admin.ModelAdmin):
    list_display=('user','book','stars_given','comment')
    list_filter=('user','id','book')
    search_fields=['user','book']

class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','bio')
    list_filter=('id','first_name','email')
    search_fields=['first_name','last_name','email']

admin.site.register(Book,BookAdmin)
admin.site.register(Book_Author,Book_AuthorAdmin)
admin.site.register(Book_Review,Book_ReviewAdmin)
admin.site.register(Author,AuthorAdmin)
# Register your models here.
