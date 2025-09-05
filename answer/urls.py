
from django.urls import path
from .views import AddAnswer, AnswerDetailView

urlpatterns = [
    path('questions/<int:id>/answers/', AddAnswer.as_view(), name='answer-create'),
    path('answers/<uuid:id>/', AnswerDetailView.as_view(), name='answer-detail'),
]
