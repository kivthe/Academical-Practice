from django.shortcuts import render
from django.http import JsonResponse
from . models import VacancyModel
from django.db import IntegrityError, transaction
from src import hhmanager
from src import hhsqlite

# Create your views here.

def get(request):
  vacancies = hhmanager.GetVacancies()
  for i in vacancies:
      hhsqlite.CreateVacancyRecord(i)
  records = VacancyModel.objects.all().values()
  hhsqlite.PrintAllVacancies()
  print('\n')
  return JsonResponse(list(records), safe=False)