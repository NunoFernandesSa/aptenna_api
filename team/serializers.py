from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = '__all__'
