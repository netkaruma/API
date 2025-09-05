from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Answer, Question

class AddAnswer(APIView):
    def post(self, request, id): 
        question = get_object_or_404(Question, id=id)
        

        if not request.user.is_authenticated:
            return Response(
                {"error": "Требуется авторизация"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        text = request.data.get('text')
        if not text:
            return Response(
                {"error": "Текст ответа обязателен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            answer = Answer.objects.create(
                question=question,
                user=request.user,
                text=text
            )
            
            return Response(
                {
                    "message": "Ответ успешно создан",
                    "answer_id": answer.id,
                    "text": answer.text
                },
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            return Response(
                {"error": f"Ошибка при создании ответа: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class AnswerDetailView(APIView):
    def get(self, request, id):
        try:
            answer = get_object_or_404(Answer, id=id)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": f"Ошибка при получении ответа: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self, request, id):
        try:
            answer = get_object_or_404(Answer, id=id)
            
            if answer.user != request.user and not request.user.is_staff:
                return Response(
                    {"error": "Вы можете удалять только свои ответы"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            answer.delete()
            return Response(
                {"message": "Ответ успешно удален"},
                status=status.HTTP_204_NO_CONTENT
            )
            
        except Exception as e:
            return Response(
                {"error": f"Ошибка при удалении ответа: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )