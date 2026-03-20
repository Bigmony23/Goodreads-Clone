from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewSerializer
from books.models import Book_Review
from rest_framework import generics
from rest_framework import viewsets


# class BookReviewViewDetailAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, id):
#         book_review=Book_Review.objects.get(id=id)
#         serializer = BookReviewSerializer(book_review)
#
#
#         # json_response={
#         #     'id':book_review.id,
#         #     'stars_given':book_review.stars_given,
#         #     "comment":book_review.comment,
#         #     'book':{
#         #         "id":book_review.book.id,
#         #         "title":book_review.book.title,
#         #         'description':book_review.book.description,
#         #         'isbn':book_review.book.isbn,
#         #     },
#         #     'user':{
#         #         "id":book_review.user.id,
#         #         'first_name':book_review.user.first_name,
#         #         'last_name':book_review.user.last_name,
#         #         'username':book_review.user.username,
#         #         'email':book_review.user.email,
#         #     }
#         #
#         # }
#         # return JsonResponse(json_response)
#         return Response(data=serializer.data)
#     def delete(self, request, id):
#         book_review=Book_Review.objects.get(id=id)
#         book_review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def put(self, request, id):
#         book_review=Book_Review.objects.get(id=id)
#         serializer = BookReviewSerializer(book_review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         book_review = Book_Review.objects.get(id=id)
#         serializer = BookReviewSerializer(book_review, data=request.data, partial=True) # only one change
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookReviewSerializer
    queryset = Book_Review.objects.all().order_by('-created_at')
    lookup_field = 'id'
# class BookReviewViewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = BookReviewSerializer
#     queryset = Book_Review.objects.all()
#     lookup_field = 'id'


# class BookReviewListAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#
#         book_reviews=Book_Review.objects.all().order_by('-created_at')
#         pagination = PageNumberPagination()
#         pag_obj = pagination.paginate_queryset(book_reviews,request)
#         serializer = BookReviewSerializer(pag_obj, many=True)
#         return pagination.get_paginated_response(serializer.data)
#
#     def post(self, request):
#         serializer = BookReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # Create your views here.

# class BookReviewListAPIView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = BookReviewSerializer
#     queryset = Book_Review.objects.all().order_by('-created_at')

