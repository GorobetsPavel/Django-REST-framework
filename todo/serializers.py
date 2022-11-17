from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('project_name', 'repository', 'users',)
# class ProjectModelSerializer(HyperlinkedModelSerializer):ModelSerializer
#     class Meta:
#         model = Project
#         fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ('project', 'text', 'user', 'active',)
