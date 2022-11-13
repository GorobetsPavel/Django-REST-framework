from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authapp.views import CustomUserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet


router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
