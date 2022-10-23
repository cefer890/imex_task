from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from tasks.models import ManageTask
from tasks.serializers import TaskSerializer


class TaskApiView(ListAPIView):
        serializer_class = TaskSerializer
        name = 'task-list'
        permission_classes = (IsAuthenticated,)

        def get_queryset(self):
            return ManageTask.objects.filter(user=self.request.user)