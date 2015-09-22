from django.db import models


            
class CustomChoiceField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 50
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        
    def to_python(self, value):
        if value is None:
            return None
            
        elif value == 1:
             str_val = 'Rail Base Case'
             return str_val 
           
        elif value == 2:
             str_val = 'Rail Traffic Working'
             return str_val
             
        elif value == 3:
             str_val = 'RL Final'
             return str_val   
              
        else:
            raise ValueError
    
    def get_prep_value(self, value):
        if value is None:
            return None
            
        elif value:
             return 1
             
        elif value:
             return 2
             
        else:
            return 3        
    

