from rest_framework import generics

from configurations.models import Configuration
from products.models import ProductQuestion
from products.serializers import ProductQuestionSerializer

from .models import Question
from .serializers import QuestionSerializer


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        configuration_id = self.kwargs.get("configuration_id")
        configuration = Configuration.objects.get(id=configuration_id)

        product_question = ProductQuestion.objects.filter(product=configuration.product)
        serializer = ProductQuestionSerializer(product_question, many=True)

        queryset = []

        for item in serializer.data:
            question_id = item["question"]
            question = Question.objects.get(id=question_id)
            queryset.append(question)

        return queryset
