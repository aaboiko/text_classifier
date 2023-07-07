from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    html = render_to_string('index.html', {'title': "Text Classifer", 'author': "Anatoliy"})
    return HttpResponse(html)

@csrf_exempt
def getres(request):
    text = request.body
    
    obj = {}
    obj["bin"] = "hjh"
    obj["num"] = 44
    return HttpResponse(json.dumps(obj), content_type="application/json")

