from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def api_index(request):
    return JsonResponse({
        "status": 200,
        "msg": "this url is working",
        "associated_people": [
            "Sourav Ganguly", "Ratul Rakshit", "Ankita Gupta"
        ],
        "associated_with": "College",
        "college_name": "SETGOI",
        "starting_date": "03/01/2022",
        "ending_date": "17/01/2022",
        "project_name": "T Shirt Selling Store",
        "technology_used": "Django, Django REST framework, Reactjs"
    })
