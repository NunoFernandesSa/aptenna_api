from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team.models import Team
from team.serializers import TeamSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getTeam(request):
    """
    Get all team elements
    Args:
        request ():

    Returns: JSON with all team elements or 404 status

    """
    if request.method == 'GET':
        try:
            team = Team.objects.all().order_by('fname')
            team_serializer = TeamSerializer(team, many=True)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(team_serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getTeamByName(request, name, ):
    """
    Get Team element by name
    Args:
        name (): String
        request ():

    Returns: JSON with one team element or 404 status

    """
    if request.method == 'GET':
        try:
            team_name = Team.objects.get(fname=name)
            name_serializer = TeamSerializer(team_name, many=False)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(name_serializer.data)
