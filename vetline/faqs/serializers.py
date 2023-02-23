from rest_framework import serializers

from vetline.faqs.models import Faqs


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"
