from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewSerializer
from books.models import Book_Review


class BookReviewViewDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id):
        book_review=Book_Review.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)


        # json_response={
        #     'id':book_review.id,
        #     'stars_given':book_review.stars_given,
        #     "comment":book_review.comment,
        #     'book':{
        #         "id":book_review.book.id,
        #         "title":book_review.book.title,
        #         'description':book_review.book.description,
        #         'isbn':book_review.book.isbn,
        #     },
        #     'user':{
        #         "id":book_review.user.id,
        #         'first_name':book_review.user.first_name,
        #         'last_name':book_review.user.last_name,
        #         'username':book_review.user.username,
        #         'email':book_review.user.email,
        #     }
        #
        # }
        # return JsonResponse(json_response)
        return Response(data=serializer.data)



class BookReviewListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):

        book_reviews=Book_Review.objects.all().order_by('-created_at')
        pagination = PageNumberPagination()
        pag_obj = pagination.paginate_queryset(book_reviews,request)
        serializer = BookReviewSerializer(pag_obj, many=True)
        return pagination.get_paginated_response(serializer.data)
# Create your views here.
