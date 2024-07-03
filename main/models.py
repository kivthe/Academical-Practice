from django.db import models

# Create your models here.

class VacancyModel(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=128)
  area_id = models.CharField(max_length=64)
  area_name = models.CharField(max_length=128)
  data_updated = models.DateTimeField('date updated')

  def __str__(self):
    return self.name

