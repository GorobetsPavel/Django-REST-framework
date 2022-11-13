from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    project_name = models.CharField(max_length=150, verbose_name='Title')
    repository = models.URLField()
    users = models.ManyToManyField(get_user_model())
    create_date = models.DateTimeField(_("date added"), auto_now_add=True)
    deleted = models.BooleanField(default=False)

    EMAIL_FIELD = "project_name"
    REPOSITORY = "repository"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Project")
        ordering = ("-create_date",)


class Todo(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("Project"))
    text = models.TextField(verbose_name="Text", blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    create_date = models.DateTimeField(_("date added"), auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name="Update", editable=False)
    active = models.BooleanField(default=False)

    PROJECT = "Project"
    CREATE_DATE = "create date"

    def close(self, *args):
        self.active = False
        self.save()

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Project")
        ordering = ("-create_date",)
