from rest_framework import fields, serializers

from tasks.models import ManageTask


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ManageTask
        fields = ['title', 'description', 'created_at', 'deadline']