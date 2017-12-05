from rest_framework import generics, mixins
from inventory.models import Task
from inventory.serializer import TaskSerializer


class TaskAPI(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, requset, *args, **kwargs):
        return self.create(requset, *args, **kwargs)
