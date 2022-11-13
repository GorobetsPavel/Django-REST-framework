from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from .models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = StringRelatedField(many=True)
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('project_name', 'repository', 'users',)


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ('project', 'text', 'user', 'active',)
