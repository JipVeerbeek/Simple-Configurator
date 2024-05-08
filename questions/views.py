from rest_framework import generics
from .models import Question
from products.models import ProductQuestion
from .serializers import QuestionSerializer
from products.serializers import ProductQuestionSerializer


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')

        product_question = ProductQuestion.objects.filter(product_id=product_id)
        serializer = ProductQuestionSerializer(product_question, many=True)

        queryset = []

        for item in serializer.data:
            question_id = item['question_id']
            question = Question.objects.get(id=question_id)
            queryset.append(question)

        return queryset
