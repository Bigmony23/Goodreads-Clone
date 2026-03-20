from django.urls import path
from api.views import BookReviewViewSet
# from .views import BookReviewViewDetailAPIView,BookReviewListAPIView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
app_name="api"
router.register('reviews', BookReviewViewSet, basename='reviews')
urlpatterns = router.urls
# urlpatterns=[
# path('reviews/',BookReviewListAPIView.as_view(),name='reviews-list'),
#    path('reviews/<int:id>/',BookReviewViewDetailAPIView.as_view(),name='review-detail')
#
# ]