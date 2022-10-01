from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    email = models.EmailField(max_length=50)
    name_surname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    edit_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'Contact'
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'

    def __str__(self):
        return self.email
