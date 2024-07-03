from django.db.utils import OperationalError
from main.models import VacancyModel
import hhtypes

#--------------------------------------------------

def CreateVacancyRecord(vacancy=hhtypes.Vacancy) -> bool:
  new_record = VacancyModel(id=vacancy.id,
                            name=vacancy.name,
                            area_id=vacancy.area.id,
                            area_name=vacancy.area.name,
                            salary_max=vacancy.salary.max,
                            salary_min=vacancy.salary.min,
                            salary_currency=vacancy.salary.currency,
                            salary_gross=vacancy.salary.gross,
                            experience_id=vacancy.experience.id,
                            experience_name=vacancy.experience.name,
                            url=vacancy.url,
                            alternate_url=vacancy.alternate_url)
  new_record.save(force_insert=True)

#--------------------------------------------------

def CheckVacancyModelExistence() -> bool:
    try:
        VacancyModel.objects.exists()
        return True
    except OperationalError:
        return False

#--------------------------------------------------

def GetVacancyFromModel(primary_key: hhtypes.Vacancy.id) -> hhtypes.Vacancy:
  if not CheckVacancyModelExistence(): return hhtypes.Vacancy()
  try:
    object = VacancyModel.objects.get(pk=primary_key)
    vacancy = hhtypes.Vacancy
    vacancy.id = object.id
    vacancy.name = object.name
    vacancy.area.id = object.area_id
    vacancy.area.name = object.area_name
    vacancy.salary.max = object.salary_max
    vacancy.salary.min = object.salary_min
    vacancy.salary.currency = object.salary_currency
    vacancy.salary.gross = object.salary_gross
    vacancy.experience.id = object.experience_id
    vacancy.experience.name = object.experience_name
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