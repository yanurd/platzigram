#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json

def hello_world(request):
  now  = datetime.now().strftime('%b %dth, %Y - %I:%M %p')
  return HttpResponse('Oh, Hi!, current server time is: {now}'.format(now=str(now)))

def hi(request):

  numbers = request.GET['numbers']
  sort = sorted([int(number) for number in numbers.split(',')])
  response = json.dumps({"numbers": sort})
  return HttpResponse(str(sort))