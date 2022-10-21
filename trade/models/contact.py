from django.db import models
from ckeditor.fields import RichTextField
from trade.abstract_models import DateAbstractModel


class Contact(DateAbstractModel):
    email = models.EmailField(max_length=50)
    name_surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = RichTextField()

    class Meta:
        db_table = 'Contact'
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'

    def __str__(self):
        return self.email
