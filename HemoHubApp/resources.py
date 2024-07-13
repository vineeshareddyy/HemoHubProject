from import_export import resources
from .models import PersonData

class PersonDataResource (resources.ModelResource):
    class Meta:
        model=PersonData