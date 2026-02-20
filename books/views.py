from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book

#
def books_list(request):
    books_all = Book.objects.all()
    context = {'books_all': books_all}
    return render(request,'list_of_books.html',context=context)

#CRUD




class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        page_size=request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)
        page_num=request.GET.get('page',1)
        page_obj=paginator.get_page(page_num)
        context = {'page_obj': page_obj}
        return render(request,'list_of_books.html',context=context)

# class BookListView(ListView):
#     template_name="list_of_books.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 2



# class BookDetailView(View):
#     def get(self, request,id):
#         book = Book.objects.get(id=id)
#         context = {'book': book}
#         return render(request,"detail.html",context=context)

class BookDetailView(DetailView):
    template_name="detail.html"
    pk_url_kwarg = "id"
    model = Book

# Create your views here.
