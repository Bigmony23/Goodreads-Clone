from django.contrib import admin
from django.urls import path
from .views import books_list, BookListView, BookDetailView, AddReview, EditReviewView,ConfirmDeleteReview,DeleteReview

urlpatterns=(
    path('books/', books_list, name='book-list'),
    path('list/', BookListView.as_view(), name='book-list'),
    path("<int:id>/", BookDetailView.as_view(), name='book-detail'),
    path('<int:id>/reviews/', AddReview.as_view(), name='addreviews'),
    path('<int:book_id>/reviews/<int:review_id>/edit/', EditReviewView.as_view(), name='reviews_edit'),
    path('<int:book_id>/reviews/<int:review_id>/delete/confirm', ConfirmDeleteReview.as_view(), name='reviews_delete_confirm'),
    path('<int:book_id>/reviews/<int:review_id>/delete/', DeleteReview.as_view(), name='reviews_delete')

)