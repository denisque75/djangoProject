from django.http import JsonResponse, HttpResponse, HttpRequest, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, ParseError
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView


class BaseQuestionView(APIView):
    def get_serializer_context(self, request):
        return { 'request': request, }


class QuestionList(BaseQuestionView):
    """
     List all code question, or create a new question.
    """
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer_context = self.get_serializer_context(request=request)
        serializer = QuestionSerializer(questions, many=True, context=serializer_context)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer_context = self.get_serializer_context(request=request)
        serializer = QuestionSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class QuestionDetails(BaseQuestionView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_question(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        question = self.get_question(pk=pk)
        serializer_context = self.get_serializer_context(request=request)
        serializer = QuestionSerializer(question, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_question(pk=pk)
        serializer_context = self.get_serializer_context(request=request)
        serializer = QuestionSerializer(question, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        question = self.get_question(pk=pk)
        serializer_context = self.get_serializer_context(request=request)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def question_list(request: HttpRequest):
#     """
#     List all code question, or create a new question.
#     """
    
#     if request.method == 'GET':
#         question_list = Question.objects.all()
#         serializer = QuestionSerializer(question_list, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def question_details(request, pk: int):
#     """
#     Retrieve, update or delete a code snippet.
#     """

#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer_context = { 'request': request, }
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question, context=serializer_context)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data, context=serializer_context)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
