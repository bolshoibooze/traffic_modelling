from django.db import models
from django.db.models import *

# see: http://stackoverflow.com/questions/8683203/django-orm-can-i-have-a-booleanfield-associated-to-a-char-column-in-the-databas


class CustomBooleanField(models.NullBooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 1
        super(CustomBooleanField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value is None:
            return None
        elif value in ('Y', 'y','Yes','yes'):
            return True
        elif value in ('N', 'n','No','no'):
            return False
        else:
            raise ValueError

    def get_prep_value(self, value):
        if value is None:
            return None
        elif value:
            return 'Y'
        else:
            return 'N'
