from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.http import HttpResponse
import json
from . models import VacancyModel
from django.db import IntegrityError, transaction
from src import hhmanager
from src import hhsqlite

# Create your views here.

#------------------------------------------------------------

def refresh(request: HttpRequest) -> HttpResponse:
  try:
    vacancies = hhmanager.GetVacancies()
    added = 0
    for i in vacancies:
      if hhsqlite.CreateVacancyRecord(i):
        added += 1
    return JsonResponse({'status': 'success'})
  except:
    return JsonResponse({'status': 'failure'})

#------------------------------------------------------------

def query(request: HttpRequest) -> HttpResponse:
  try:
    #data = json.loads(request.body)
    if not hhsqlite.CheckVacancyModelExistence():
      return JsonResponse({'status': 'failure'})
    records = VacancyModel.objects.all().values()
    return JsonResponse(list(records), safe=False)
  
  except json.JSONDecodeError:
    return JsonResponse({'status': 'failure','message': 'failed to extract JSON from request\'s body'})

  except:
    return JsonResponse({'status': 'failure'})

#------------------------------------------------------------

def main(request: HttpRequest) -> HttpResponse:
  vacancies = hhmanager.GetVacancies()
  for i in vacancies:
    hhsqlite.CreateVacancyRecord(i)
  records = VacancyModel.objects.all().values()
  return JsonResponse(list(records), safe=False)

#------------------------------------------------------------