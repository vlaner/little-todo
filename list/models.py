from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse


class ToDoListModel(models.Model):
    title = models.CharField(max_length=70)
    isDone = models.BooleanField(default=False)
    user = models.ForeignKey(
        get_user_model(), default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
