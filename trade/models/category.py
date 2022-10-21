from django.db import models
from autoslug import AutoSlugField
from trade.abstract_models import DateAbstractModel
# from ckeditor.fields import RichTextField


class Category(DateAbstractModel):
    name = models.CharField(max_length=200)
    # title = models.CharField(max_length=200)
    # title_image = models.ImageField()
    slug = AutoSlugField(populate_from='name', unique=True)
    open_items_another_tab = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name or 'anonymous'


# def get_absolute_url(self):
# return f"/productdetail/{self.slug}"
