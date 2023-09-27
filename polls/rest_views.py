from django.http import JsonResponse, HttpResponse, HttpRequest, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, ParseError
from rest_framework import status, mixins, generics
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView


class BaseQuestionView(generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionList(mixins.ListModelMixin, mixins.CreateModelMixin, BaseQuestionView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class QuestionDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, BaseQuestionView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
