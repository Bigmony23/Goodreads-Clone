from django.urls import path
from .views import BookReviewViewDetailAPIView,BookReviewListAPIView
urlpatterns=[
path('reviews/',BookReviewListAPIView.as_view(),name='reviews-list'),
   path('reviews/<int:id>/',BookReviewViewDetailAPIView.as_view(),name='review-detail')

]