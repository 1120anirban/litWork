from rest_framework import serializers
from litWorks.models import LitWork

# LitWork Serializer
class LitWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LitWork
        fields = '__all__'