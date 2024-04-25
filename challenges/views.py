from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january": "Make a monthly challenge",
    "february": "Hibernate",
    "march": "Stand in the sun",
    "april": "Learn Python",
    "may": "Find a job",
    "june": "Read a book",
    "july": "Invent a recipe",
    "august": "Exercise everyday",
    "september": "Go to the beach",
    "october": "Do one spooky thing everyday",
    "november": "Be thankful",
    "december": "Be kind",
}


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("Hey! That's not a real month!")
