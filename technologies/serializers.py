from rest_framework import serializers

from technologies.models import Technologie


class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologie
        fields = '__all__'
