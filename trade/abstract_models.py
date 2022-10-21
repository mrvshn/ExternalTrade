from django.db import models


class DateAbstractModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    edit_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
