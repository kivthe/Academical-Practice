from django.db.utils import OperationalError
from main.models import VacancyModel
from src import hhtypes

#--------------------------------------------------

def CreateVacancyRecord(vacancy=hhtypes.Vacancy) -> None:
  new_record = VacancyModel(id=vacancy.id,
                            name=vacancy.name,
                            area_id=vacancy.area_id,
                            area_name=vacancy.area_name,
                            salary_max=vacancy.salary_max,
                            salary_min=vacancy.salary_min,
                            salary_currency=vacancy.salary_currency,
                            salary_gross=vacancy.salary_gross,
                            experience_id=vacancy.experience_id,
                            experience_name=vacancy.experience_name,
                            url=vacancy.url,
                            alternate_url=vacancy.alternate_url
  )
  new_record.save()

#--------------------------------------------------

def CheckVacancyModelExistence() -> bool:
    try:
        VacancyModel.objects.exists()
        return True
    except OperationalError:
        return False

#--------------------------------------------------

def GetVacancyFromModel(primary_key: str) -> hhtypes.Vacancy:
  if not CheckVacancyModelExistence(): return hhtypes.Vacancy()
  try:
    object = VacancyModel.objects.get(pk=primary_key)
    vacancy = hhtypes.Vacancy
    vacancy.id = object.id
    vacancy.name = object.name
    vacancy.area_id = object.area_id
    vacancy.area_name = object.area_name
    vacancy.salary_max = object.salary_max
    vacancy.salary_min = object.salary_min
    vacancy.salary_currency = object.salary_currency
    vacancy.salary_gross = object.salary_gross
    vacancy.experience_id = object.experience_id
    vacancy.experience_name = object.experience_name
    vacancy.url = object.url
    vacancy.alternate_url = object.alternate_url
    return vacancy

  except VacancyModel.DoesNotExist:
    return hhtypes.Vacancy()
  
#--------------------------------------------------

def PrintAllVacancies() -> None:
   all = VacancyModel.objects.all()
   for item in all:
    print(item.id, item.name, item.area_name, item.salary_max, item.salary_currency, item.experience_name, item.alternate_url)