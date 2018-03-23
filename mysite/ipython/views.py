from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from mysite.Utils import utils



def embeded(request):
	return HttpResponseRedirect("http://localhost:8888/tree")