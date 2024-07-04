from django.shortcuts import render
from django.http import JsonResponse
from . models import VacancyModel
from django.db import IntegrityError, transaction
from src import hhmanager
from src import hhsqlite

# Create your views here.

def main(request):
  vacancies = hhmanager.GetVacancies()
  #print(len(vacancies),end="\n\n")
  for i in vacancies:
    hhsqlite.CreateVacancyRecord(i)
  #print(hhsqlite.GetVacancyRecordsCount(),end="\n\n")
  records = VacancyModel.objects.all().values()
  #hhsqlite.PrintAllVacancies()
  #print('\n')
  return JsonResponse(list(records), safe=False)