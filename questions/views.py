from rest_framework import generics
from .models import Question
from products.models import ProductQuestion
from .serializers import QuestionSerializer
from products.serializers import ProductQuestionSerializer
from configurations.models import Configuration


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        configuration_id = self.kwargs.get('configuration_id')
        configuration = Configuration.objects.get(id=configuration_id)

        product_question = ProductQuestion.objects.filter(product_id=configuration.product_id)
        serializer = ProductQuestionSerializer(product_question, many=True)

        queryset = []

        for item in serializer.data:
            question_id = item['question_id']
            question = Question.objects.get(id=question_id)
            queryset.append(question)

        return queryset
