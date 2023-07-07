from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
import pickle

def index(request):
    html = render_to_string('index.html', {'title': "Text Classifer", 'author': "Anatoliy"})
    return HttpResponse(html)

@csrf_exempt
def getres(request):
    text = request.body

    model = pickle.load(open("../models/model_knn_bin.sav", "rb"))
    vec = pickle.load(open("../models/vectorizer.sav", "rb"))

    bin = predict_bin(text, model, vec)
    
    obj = {}
    obj["bin"] = bin
    obj["num"] = 44
    return HttpResponse(json.dumps(obj), content_type="application/json")

def predict_bin(text, model, vec):
    text_vec = vec.transform([text])

    bin = "The review is positive"
    pred = model.predict(text_vec)
    if pred == 0:
        bin = "The review is negative"

    return bin

def predict_num(text, model, vec):
    text_vec = vec.transform(text)
    pred = model.predict(text_vec)
    return pred