from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    objects = models.Manager()

    class Meta:
        db_table = 'category'

    name = models.CharField('カテゴリー', max_length=256)

    def __str__(self):
        return self.name
  
class Knowledge(models.Model):
    objects = models.Manager()

    class Meta:
        db_table = 'knowledge'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
