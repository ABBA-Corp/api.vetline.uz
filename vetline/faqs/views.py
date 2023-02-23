from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from vetline.faqs.models import Faqs
from vetline.faqs.serializers import FaqSerializer


class FaqViewset(mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Faqs.objects.all().order_by('order')
    serializer_class = FaqSerializer
