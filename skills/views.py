from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from skills.models import Skill
from skills.serializers import SkillsSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getSkills(request):
    """
    Get all skills
    Args:
        request ():

    Returns: JSON with all skills order by id or 404 status

    """
    if request.method == 'GET':
        try:
            skills = Skill.objects.all().order_by('id')
            skills_serializer = SkillsSerializer(skills, many=True)
        except Skill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(skills_serializer.data)
