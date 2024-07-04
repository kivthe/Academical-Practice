import requests
from src import hhtypes
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
      hhvacancy.url = vacancy['url']
      hhvacancy.alternate_url = vacancy['alternate_url']
      if vacancy['area'] is not None:
        hhvacancy.area_id   = vacancy['area']['id']
        hhvacancy.area_name = vacancy['area']['name']
      if vacancy['salary'] is not None:
        hhvacancy.salary_min = vacancy['salary']['from']
        hhvacancy.salary_max = vacancy['salary']['to']
        hhvacancy.salary_currency = vacancy['salary']['currency']
        hhvacancy.salary_gross = vacancy['salary']['gross']
      #if vacancy['type'] is not None:
        #hhvacancy.type = hhtypes.IDName
        #hhvacancy.type.id = vacancy['type']['id']
        #hhvacancy.type.name = vacancy['type']['name']
      if vacancy['experience'] is not None:
        hhvacancy.experience_id   = vacancy['experience']['id']
        hhvacancy.experience_name = vacancy['experience']['name']
      vacancies.append(copy.deepcopy(hhvacancy))
  return vacancies
#--------------------------------------------------
