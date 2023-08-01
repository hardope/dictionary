from rest_framework import serializers
from .models import Word

class WordSerializer(serializers.Serializer):

     class Meta:
          fields = '__all__'
          model = Word

     def create(self, validated_data):
          return Word.objects.create(**validated_data)