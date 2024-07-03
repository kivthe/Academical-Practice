import requests
import json
import hhtypes
import copy

hhvacancies = 'http://api.hh.ru/vacancies'
hhemployers = 'http://api.hh.ru/employers'
hhareas     = 'http://api.hh.ru/areas'

#--------------------------------------------------
def GetVacancyCount(self) -> int:
  response = requests.get(hhvacancies)
  if response.ok:
    return response.json().get('found')
  else:
    return -1
#--------------------------------------------------
def GetEmployerCount(self) -> int:
  response = requests.get(hhemployers)
  if response.ok:
    return response.json().get('found')
  else:
    return -1
#--------------------------------------------------
def GetVacancies() -> list[hhtypes.Vacancy]:
  response = requests.get(hhvacancies)
  if not response.ok: return list()
  pages_count = response.json().get('pages')
  pages_count //= 50
  vacancies = list()
  for i in range(pages_count):
    params = {'page' : i}
    response = requests.get(hhvacancies,params=params)
    if not response.ok: break
    json_file = response.json()
    for vacancy in json_file['items']:
      hhvacancy = hhtypes.Vacancy
      hhvacancy.id = vacancy['id']
      hhvacancy.name = vacancy['name']
      hhvacancy.hast_test = vacancy['has_test']
      if vacancy['area'] is not None:
        hhvacancy.area = hhtypes.Area
        hhvacancy.area.id = vacancy['area']['id']
        hhvacancy.area.name = vacancy['area']['name']
        hhvacancy.area.url = vacancy['area']['url']
      if vacancy['salary'] is not None:
        hhvacancy.salary = hhtypes.Salary
        hhvacancy.salary.min = vacancy['salary']['from']
        hhvacancy.salary.max = vacancy['salary']['to']
        hhvacancy.salary.currency = vacancy['salary']['currency']
        hhvacancy.salary.gross = vacancy['salary']['gross']
      if vacancy['type'] is not None:
        hhvacancy.type = hhtypes.IDName
        hhvacancy.type.id = vacancy['type']['id']
        hhvacancy.type.name = vacancy['type']['name']
      if vacancy['experience'] is not None:
        hhvacancy.type = hhtypes.IDName
        hhvacancy.type.id = vacancy['experience']['id']
        hhvacancy.type.name = vacancy['experience']['name']
      vacancies.append(copy.deepcopy(hhvacancy))
  return vacancies
#--------------------------------------------------
vacancies = GetVacancies()
print(len(vacancies))
for i in vacancies:
  print(i.name, i.area.name, end="\n")
