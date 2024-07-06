import requests
from src import hhtypes
import copy

#--------------------------------------------------

hhvacancies = 'http://api.hh.ru/vacancies'
hhemployers = 'http://api.hh.ru/employers'
hhareas     = 'http://api.hh.ru/areas'

#--------------------------------------------------

# Vacancy key skills collection skills
# Pros: More information
# Cons: More response time and routing

collect_key_skills = True

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
  # Hard-coded limiter to how many pages the program can request
  pages_count //= 10
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
        hhvacancy.area_id   = vacancy['area']['id']
        hhvacancy.area_name = vacancy['area']['name']
      if vacancy['salary'] is not None:
        hhvacancy.salary_min = vacancy['salary']['from']
        hhvacancy.salary_max = vacancy['salary']['to']
        hhvacancy.salary_currency = vacancy['salary']['currency']
        hhvacancy.salary_gross = vacancy['salary']['gross']
      if vacancy['type'] is not None:
        hhvacancy.type_id = vacancy['type']['id']
        hhvacancy.type_name = vacancy['type']['name']
      if vacancy['address'] is not None:
        hhvacancy.address_raw = vacancy['address']['raw']
      hhvacancy.url = vacancy['url']
      hhvacancy.alternate_url = vacancy['alternate_url']
      if vacancy['snippet'] is not None:
        hhvacancy.snippet_requirement = vacancy['snippet']['requirement']
        hhvacancy.snippet_responsibility = vacancy['snippet']['responsibility']
      if vacancy['schedule'] is not None:
        hhvacancy.schedule_id = vacancy['schedule']['id']
        hhvacancy.schedule_name = vacancy['schedule']['name']
      if vacancy['experience'] is not None:
        hhvacancy.experience_id   = vacancy['experience']['id']
        hhvacancy.experience_name = vacancy['experience']['name']
      if vacancy['employment'] is not None:
        hhvacancy.employemnt_id = vacancy['employment']['id']
        hhvacancy.employment_name = vacancy['employment']['name']
      hhvacancy.key_skills = list()
      if hhvacancy.url and collect_key_skills:
        response = requests.get(hhvacancy.url)
        if response.ok:
          file = response.json()
          for skill in file['key_skills']:
            hhvacancy.key_skills.append(skill['name'])
            #print(skill['name'])

      vacancies.append(copy.deepcopy(hhvacancy))
  return vacancies
#--------------------------------------------------

def CheckFilterJson(json_data) -> bool:
  return (json_data['salary_min'] is not None) and (json_data['salary_max'] is not None) and (json_data['salary_currency'] is not None) and (json_data['area_id'] is not None) and (json_data['expereince_id'] is not None)

#--------------------------------------------------