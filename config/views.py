from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book, Book_Review


def landing_page(request):
    return render(request,'landing.html')

def home_page(request):
    books_reviews = Book_Review.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size',10)
    paginator = Paginator(books_reviews, page_size)
    page_num=request.GET.get('page',1)
    page_obj = paginator.page(page_num)
    context = {'page_obj': page_obj}
    return render(request,'home.html',context)
