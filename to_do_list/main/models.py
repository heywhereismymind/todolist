from django.db import models


class To_Do_List(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    task_name = models.CharField(unique=True)
    task_description = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True)
