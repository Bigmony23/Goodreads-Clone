from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from books.forms import ReviewForm
from books.models import Book, Book_Review


#
def books_list(request):
    books_all = Book.objects.all()
    context = {'books_all': books_all}
    return render(request,'list_of_books.html',context=context)

#CRUD




class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q','')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size=request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)
        page_num=request.GET.get('page',1)
        page_obj=paginator.get_page(page_num)
        context = {'page_obj': page_obj,"search_query":search_query}
        return render(request,
                      'list_of_books.html',
                      context=context)

# class BookListView(ListView):
#     template_name="list_of_books.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 2



class BookDetailView(View):
    def get(self, request,id):
        book = Book.objects.get(id=id)
        review_form=ReviewForm()
        context = {'book': book, 'review_form': review_form}

        return render(request,"detail.html",context=context)


# class BookDetailView(DetailView):
#     template_name="detail.html"
#     pk_url_kwarg = "id"
#     model = Book

class AddReview(LoginRequiredMixin,View):
    def post(self,request,id):
        book=Book.objects.get(id=id)
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            Book_Review.objects.create(
                book=book,
                user=request.user,
                comment=review_form.cleaned_data['comment'],
                stars_given=review_form.cleaned_data['stars_given'],


            )
            return redirect(reverse('book-detail',kwargs={'id':book.id}))
        return redirect(request,'books/detail.html',{"book":book,"review_form":review_form})



# Create your views here.
