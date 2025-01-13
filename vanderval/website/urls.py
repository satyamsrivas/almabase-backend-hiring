from django.urls import path
from .views import EnqueueJobView

urlpatterns = [
     path("enqueue-task",EnqueueJobView.as_view(),name='enqueuetask')
]

