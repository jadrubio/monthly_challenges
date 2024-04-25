from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized}</a></li>"
    response_data= f"<ul>{list_items}</ul>"
    return HttpResponse(response_data, content_type="text/html")

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1 or month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("Hey! That's not a real month!")
