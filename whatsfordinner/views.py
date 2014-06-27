#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
	hello = "Hello"
	return render_to_response('index.html', {'hello': hello}, context_instance=RequestContext(request))