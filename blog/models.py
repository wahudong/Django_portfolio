from django.db import models

# Create your models here.
class Blog(models.Model):
  """
  model of blog
  """
  title=models.CharField(max_length=200)
  description = models.TextField()
  date = models.DateField()


