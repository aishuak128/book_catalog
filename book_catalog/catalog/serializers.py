from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'published', 'author')


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(default='')
    author_id = serializers.IntegerField(default=None)
    # author потом поменять на CharField()
    published = serializers.DateField(default=None)
    created= serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author)
        instance.published = validated_data.get('published', instance.published)
        instance.modified = validated_data.get('modified', instance.modified)
        instance.save()

        return instance

