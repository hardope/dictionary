from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WordSerializer
from .models import Word

# Create your views here.
class SearchWord(APIView):
     
     def get(self, request, query):
          word = Word.objects.filter(word=query)
          serializer = WordSerializer(word, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)

class GetWord(APIView):

     def get(self, request, query):
          try:
               word = Word.objects.get(word=query)
               serializer = WordSerializer(word)
               return Response(serializer.data, status=status.HTTP_200_OK)
          except Word.DoesNotExist:
               return Response(status=status.HTTP_404_NOT_FOUND)
