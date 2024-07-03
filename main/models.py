from django.db import models

# Create your models here.

class VacancyModel(models.Model):
  id = models.CharField(max_length=64, primary_key=True)
  name = models.CharField(max_length=64)
  area_id = models.CharField(max_length=64)
  area_name = models.CharField(max_length=64)
  salary_max = models.CharField(max_length=32)
  salary_min = models.CharField(max_length=32)
  salary_currency = models.CharField(max_length=32)
  salary_gross = models.BooleanField()
  experience_id = models.CharField(max_length=64)
  experience_name = models.CharField(max_length=64)
  url = models.CharField(max_length=256)
  alternate_url = models.CharField(max_length=256)

  def __str__(self):
    return self.name

