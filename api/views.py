
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewSerializer
from books.models import Book_Review


class BookReviewViewDetailAPIView(APIView):
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
    def get(self, request):
        book_reviews=Book_Review.objects.all()
        serializer = BookReviewSerializer(book_reviews, many=True)
        return Response(data=serializer.data)
# Create your views here.
