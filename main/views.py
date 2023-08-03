from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mymodel import *

# Create your views here.
class SearchWord(APIView):
     
     def get(self, request, query):
          word = search_word(query)
          if word:
               return Response(word, status=status.HTTP_200_OK)
          else:
               return Response(status=status.HTTP_404_NOT_FOUND)

class GetWord(APIView):

     def get(self, request, query):
          word = get_word(query)
          if word:
               return Response(word, status=status.HTTP_200_OK)
          else:
               return Response(status=status.HTTP_404_NOT_FOUND)

class RandomWord(APIView):

     def get(self, request):
          word = get_random()
          return Response(word, status=status.HTTP_200_OK)
