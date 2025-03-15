from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from .lambda_simulation import lambda_simulation
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet,):
    """_summary_
       This viewset provides CRUD operations for tasks, including custom actions
       like marking a task as completed. Additionally, the viewset allows filtering tasks
       by their status and handles the assignment of the user responsible for the task.

    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Rate-limiting: Users can only make 5 requests per minute(implement this
    # if you want to implement throttling to this view only now throttling is 
    # througn settings.py)
    # throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        
        if status:

            return self.queryset.filter(status=status)
        
        return self.queryset
    def perform_create(self, serializer):
        
        user = self.request.data.get('user', None)
        
        if user:
            
            serializer.save(user_id=user)
        else:
            
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
       
        user = self.request.data.get('user', None)
        
        if user:
            
            serializer.save(user_id=user)
        else:
            
            serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """_summary_

       This custom action allows users to mark a task as completed by setting the task's 
        `status` field to 'completed'
        """
        task = self.get_object()
        task.status = 'completed'
        task.save()
        
        # Simulate Lambda Notification
        lambda_simulation("completed")
        
        return Response(
            {
                "status": "success",
            }
        )
