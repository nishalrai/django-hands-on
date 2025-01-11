from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

'''
def january(request):
	return HttpResponse("Hello, this is the month of January")

def feburary(request):
	return HttpResponse("Month of Feburary")
'''
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

'''
def monthly_challenge_by_number(request, month):
	return HttpResponse(month)
'''


'''
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

	# "<li><a href="...">January</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

'''


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # /challenge/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    # when user send the request /challenges/janauary
    try:
        challenge_text = monthly_challenges[month]
        # This will extract the value of the corresponding input month value
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenges.html")
        # response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
        # return HttpResponse(challenge_text)
    except:
        raise Http404()
        #return HttpResponseNotFound("<h1>This month is not supported!</h1>")


'''
def monthly_challenge(request, month):
	challenge_text = None
	if month == "january":
		challenge_text = "Eat no meat for the entire month!"
	elif month == "february":
		challenge_text = "walk for at least 20 minutes every day!"
	elif month == "march":
		challenge_text = "Learn Django for at least 20 minutes every day!"
	else:
		return HttpResponseNotFound("This month is not supported!")
	return HttpResponse(challenge_text)
'''
