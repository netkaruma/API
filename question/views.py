from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from answer.models import Answer
from answer.serializers import AnswerSerializer
from .serializers import QuestionSerializer
from .models import Question


class QuestionsListView(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    def get(self, request, id):
        try:
            question = Question.objects.get(id=id)
        except Question.DoesNotExist:
            return Response(
                {"success": False, "message": f"Вопрос с id {id} не найден"},
                status=status.HTTP_404_NOT_FOUND
            )

        answers = Answer.objects.filter(question=question)
        question_serializer = QuestionSerializer(question)
        answers_serializer = AnswerSerializer(answers, many=True)

        return Response({
            'question': question_serializer.data,
            'answers': answers_serializer.data
        })
    
    def delete(self, request, id):
        try:
            question = Question.objects.get(id=id)
            question.delete()
            return Response(
                {"success": True, "message": f"Вопрос с id {id} удален"},
                status=status.HTTP_200_OK
            )
        except Question.DoesNotExist:
            return Response(
                {"success": False, "message": f"Вопрос с id {id} не найден"},
                status=status.HTTP_404_NOT_FOUND
            )