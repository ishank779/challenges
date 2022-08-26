from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
#from django.template.loader import render_to_string

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

def index(request):
    list_items=""
    months=list(monthly_challenges.keys())
    '''for i in months:
        month_path=reverse("month-challenge",args=[i])
        list_items+=f"<li><a href=\"{month_path}\">{i.capitalize()}</a></li>"
    response_data=f"<ul>{list_items}</ul>"'''
    return render(request,"challenges/index.html",{
        "months":months
    })
def challenges(request,month):

    try:
        return_text=monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":return_text,
            "month_name": month#.capitalize()
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        return HttpResponse("invalid month")
def challenges_int(request,month):
    months=list(monthly_challenges.keys())
    print(len(months))
    if month>len(months):
        return HttpResponseNotFound()
    redirect_month=str(months[month-1])
    redirect_path=reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

'''def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenge[month]
        response_data=render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound()'''