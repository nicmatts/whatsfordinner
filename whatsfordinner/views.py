#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from meals.models import Meal

def home(request):
	all_meals = Meal.all_meals.all()
	return render_to_response('index.html', {'all_meals': all_meals}, context_instance=RequestContext(request))