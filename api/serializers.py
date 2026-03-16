from rest_framework import serializers


from books.models import Book, Book_Review
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     isbn=serializers.CharField(max_length=17)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     username = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=255)

class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book_Review
        fields = '__all__'


# class BookReviewSerializer(serializers.Serializer):
#     stars_given = serializers.IntegerField(min_value=1, max_value=5)
#     comment=serializers.CharField()
#     book = BookSerializer()
#     user = UserSerializer()

