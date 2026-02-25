from django.contrib import admin
from django.urls import path
from .views import books_list, BookListView, BookDetailView,AddReview

urlpatterns=(
    path('books/', books_list, name='book-list'),
    path('list/', BookListView.as_view(), name='book-list'),
    path("<int:id>/", BookDetailView.as_view(), name='book-detail'),
    path('<int:id>/reviews/', AddReview.as_view(), name='addreviews'),

)