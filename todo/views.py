from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')

        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


# class ProjectAPIView(APIView):
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request, format=None):
#         projects = Project.objects.all()
#         pk = req
#         serializer = ProjectModelSerializer(projects, many=True)
#         return Response(serializer.data)
#
#
# class TodoAPIView(APIView):
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request, format=None):
#         notes = Todo.objects.all()
#         serializer = TodoModelSerializer(notes, many=True)
#         return Response(serializer.data)
#
#     def delete(self,  request, format=None):
#         pass

