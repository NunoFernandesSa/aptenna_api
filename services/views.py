from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ServicesSerializer
from .models import Service


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getServices(request):
    """
    Get all services
    Args:
        request ():

    Returns: JSON with all services order by id or 404 status

    """
    if request.method == 'GET':
        try:
            services = Service.objects.all().order_by('id')
            services_serializer = ServicesSerializer(services, many=True)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(services_serializer.data)
