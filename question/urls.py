from django.urls import path
from .views import QuestionsListView, QuestionDetailView

urlpatterns = [
    path('questions/', QuestionsListView.as_view(), name='questions-list'),
    path('questions/<int:id>/', QuestionDetailView.as_view(), name='question-detail'),
]