from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from technologies.models import Technologie
from technologies.serializers import TechnologieSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getTechnologies(request):
    """
    Get all technologies
    Args:
        request ():

    Returns: JSON with all technologies or 404 status

    """
    if request.method == 'GET':
        try:
            technologie = Technologie.objects.all().order_by('id')
            technologie_serializer = TechnologieSerializer(technologie, many=True)
        except Technologie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(technologie_serializer.data)
