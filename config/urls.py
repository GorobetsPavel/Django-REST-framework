from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authapp.views import CustomUserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
# from todo.views import ProjectAPIView, TodoAPIView, project_view, notes_view


router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/project/', ProjectAPIView.as_view()),
    # path('api/project_view/', project_view),
    # path('api/notes/', TodoAPIView.as_view()),
    # path('api/notes_view/', notes_view),

    # path('views/api-view/', views.ProjectAPIView.as_view()),
]
