from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges={
    "january":"run 20 miles",
    "february":"do 20 pushups",
    "march":"do 30 pushups",
    "april":"run 4 mile and do 20 pushups",
    "may":"take a day off",
    "june":"it's too hot run 4 miles in night",
    "july":"start gym in evening time",
    "august":"gain some muscles",
    "october":"winters are comming",
    "september":"don't hibernate",
    "november":"don't do that thing",
    "december":"celebrate your birthday"

}
'''def index(request):
    return HttpResponse("this works")
def february(request):
    return HttpResponse("run for a mile fot next 28 days")'''
def challenges(request,month):
    try:
        return_text=monthly_challenges[month]
        return HttpResponse(return_text)
    except:
        return HttpResponse("invalid month")
def challenges_int(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound()
    redirect_month=months[month-1]
    #redirect_path=reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect("challenge/"+redirect_month)

