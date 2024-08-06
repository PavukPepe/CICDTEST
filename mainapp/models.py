from django.db import models


class SimpleModel(models.Model):
    just_text = models.CharField(verbose_name='Just a field', max_length=200)