from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from website.models import Site, JobType
from website.tasks import execute_task

class EnqueueJobView(APIView):
    """
    API endpoint to enqueue a job for a customer.
    """
    def post(self, request, *args, **kwargs):
        site_id = request.data.get("site_id")
        job_type_id = request.data.get("job_type_id")

        try:
            site = Site.objects.get(id=site_id)
            job_type = JobType.objects.get(id=job_type_id)

            # Enqueue the task
            execute_task.delay(job_type_id, site_id)
            return Response({"message": "Job enqueued successfully!"}, status=status.HTTP_200_OK)
        except Site.DoesNotExist:
            return Response({"error": "Site not found."}, status=status.HTTP_404_NOT_FOUND)
        except JobType.DoesNotExist:
            return Response({"error": "Job type not found."}, status=status.HTTP_404_NOT_FOUND)
