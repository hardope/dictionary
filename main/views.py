from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mymodel import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class SearchWord(APIView):
     
     @swagger_auto_schema(
          operation_summary='Search word',
          operation_description='search for words similar to query provided',
          responses={
               200: 'OK',
               404: 'Not Found',
          }
     )
     def get(self, request, query):
          word = search_word(query)
          if word:
               return Response(word, status=status.HTTP_200_OK)
          else:
               return Response(status=status.HTTP_404_NOT_FOUND)

class GetWord(APIView):

     @swagger_auto_schema(
          operation_summary='Get word',
          operation_description='Find the word with exact match to query provided',
          responses={
               200: 'OK',
               404: 'Not Found',
          }
     )
     def get(self, request, query):
          word = get_word(query)
          if word:
               return Response(word, status=status.HTTP_200_OK)
          else:
               return Response(status=status.HTTP_404_NOT_FOUND)

class RandomWord(APIView):

     @swagger_auto_schema(
          operation_summary='Random word',
          operation_description='Get a random word',
          responses={
               200: 'OK',
          }
     )

     def get(self, request):
          res = {}
          word = get_random()
          res["message"]= "Welcome to my Dictionary API, Here's A random Word"
          res["API_DOCS"]= "mydictionary.pythonanywhere.com/docs/"
          res["word"] = word
          return Response(res, status=status.HTTP_200_OK)
