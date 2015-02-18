from django.shortcuts import render
from django.http import HttpResponse

import json
from summers.json_encoders import DateTimeEncoder

from django.core.cache import cache
from summers.models import SummationDifference

def difference(request):
    ''' Show a SummationDiffernece object as JSON.
    '''
    summer_dict = {}
    http_code=200

    if request.method == 'GET' and 'number' in request.GET:
        try:
            number_key = request.GET['number']
            number = int(number_key)
            summer = cache.get(number_key)
            if summer is None:
                summer = SummationDifference(number)
            summer.update()
            cache.set(number_key, summer, None)

            summer_dict = summer.to_dict()
        except ValueError as e:
            summer_dict = {
                'error': str(e),
            }
            http_code=400

    summer_json = json.dumps(summer_dict, cls=DateTimeEncoder)
    return HttpResponse(summer_json, content_type='application/json', status_code=http_code)
    
