from django.contrib import admin
from todo import models as todo_models


@admin.register(todo_models.Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ["project_name", "repository", "users"]
    list_filter = ["project_name"]


@admin.register(todo_models.Todo)
class TodoAdmin(admin.ModelAdmin):
    search_fields = ["project", "text", "user", "active"]
    list_filter = ["project", "active"]

