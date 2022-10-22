from rest_framework.serializers import HyperlinkedModelSerializer
from .models import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'username', 'age',)
