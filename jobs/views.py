from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from jobs.serializers import JobSerializer
from jobs.models import Job


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getJobs(request):
    """
    Get all jobs
    Args:
        request ():

    Returns: JSON with all jobs order by id or 404 status

    """
    if request.method == 'GET':
        try:
            jobs = Job.objects.all().order_by('id')
            jobs_serializer = JobSerializer(jobs, many=True)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(jobs_serializer.data)
