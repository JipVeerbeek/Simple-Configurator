from rest_framework import generics
from rest_framework.response import Response
from configurations.models import Configuration
from products.models import ProductQuestion

from .models import Question
from .serializers import QuestionSerializer


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get(self, request, configuration_id, *args, **kwargs):
        configuration = Configuration.objects.get(id=configuration_id)

        product_question = ProductQuestion.objects.filter(product=configuration.product).values_list(
            "question__id", flat=True
        )

        questions = Question.objects.filter(id__in=product_question)
        serializer = QuestionSerializer(data=questions, many=True)
        serializer.is_valid()

        return Response(serializer.data)
