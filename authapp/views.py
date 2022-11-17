from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class CustomUserAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        pk = request.query_params.get('pk')
        if pk:
            users = users.filter(id=pk)
        serializer = CustomUserModelSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pass

    def post(self, request, pk, format=None):
        pass

