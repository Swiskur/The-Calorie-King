from django.shortcuts import render, redirect
import requests
import json
from .models import CalorieResult, Macros, ApiData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, "calorieking/home.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, 'calorieking/login.html')

def sign_up(request):
    reg = UserCreationForm()
    if request.method == 'POST':
        reg = UserCreationForm(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('login')

    sign_up = {'reg':reg}
    return render(request, 'calorieking/sign_up.html', sign_up)
def logout_user(request):
    logout(request)
    return redirect('home')

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers = {'X-Api-Key':'/wVYm+vLvaIvkGtGtuQ3gw==vaHTrTLylDs0Xttx'})                
        try:
            api = json.loads(api_request.content)
            ApiData.objects.create(
                query=query,
                calories=api[0].get('calories'),
                protein=api[0].get('protein_g'),
                carbs=api[0].get('carbohydrates_total_g'),
            )
        except:
            api = "Error"
        return render(request,'calorieking/search.html',{'api':api,})
    return render(request,'calorieking/search.html')

def burner_search(request): 
    return render(request, "calorieking/burner_search.html")
def Goal(goal1):
    goal_result = int(float(goal1))
    return goal_result
def Month(month1):
    month_result = int(float(month1))
    return month_result
def Day(day1):
    day_result = int(float(day1))
    return day_result
def Year(year1):
    year_result = int(float(year1))
    return year_result
def CalAddition(meal1,meal2,meal3):
    cal_result = int(meal1) + int(meal2) +int(meal3)
    return cal_result
def CarbAddition(carb1,carb2,carb3):
    carb_result = int(carb1) + int(carb2) +int(carb3)
    return carb_result
def ProAddition(pro1,pro2,pro3):
    pro_result = int(pro1) + int(pro2) +int(pro3)
    return  pro_result
#/wVYm+vLvaIvkGtGtuQ3gw==vaHTrTLylDs0Xttx
def counter(request):
     counter_data = ApiData.objects.all().order_by('-id')[:15]
    
     if request.method == 'POST':
        meal1 = request.POST['meal1']
        meal2 = request.POST['meal2']
        meal3 = request.POST['meal3']
        carb1 = request.POST['carb1']
        carb2 = request.POST['carb2']
        carb3 = request.POST['carb3']
        pro1 = request.POST['pro1']
        pro2 = request.POST['pro2']
        pro3 = request.POST['pro3']
        goal1 = request.POST['goal1']
        month1 = request.POST['month1']
        day1 = request.POST['day1']
        year1 = request.POST['year1']
        if 'submit' in request.POST:
            cal_result = CalAddition(meal1,meal2, meal3)
            carb_result = CarbAddition(carb1,carb2, carb3)
            pro_result = ProAddition(pro1,pro2, pro3)
            goal_result = Goal(goal1)
            month_result = Month(month1)
            day_result = Day(day1)
            year_result = Year(year1)
       
            calorie_result = CalorieResult(
                meal1=meal1, meal2=meal2, meal3=meal3,
                goal1=goal1, month1=month1, day1=day1, year1=year1
            )
            calorie_result.save()
            macro_result = Macros(
                
                carb1=carb1, carb2=carb2, carb3=carb3,
                pro1=pro1, pro2=pro2, pro3=pro3
            )

            macro_result.save()
        
        return render(request,'calorieking/counter.html',{'cal_result':cal_result, 'carb_result':carb_result, 'pro_result':pro_result, 'goal_result':goal_result, 'month_result':month_result, 'day_result': day_result, 'year_result':year_result,})
     return render(request,'calorieking/counter.html',{'counter_data': counter_data})
def Goal2(goal2):
    goal_result2 = int(float(goal2))
    return goal_result2
def Month2(month2):
    month_result2 = int(float(month2))
    return month_result2
def Day2(day2):
    day_result2 = int(float(day2))
    return day_result2
def Year2(year2):
    year_result2 = int(float(year2))
    return year_result2
def CalBurnedAddition(burn1, burn2, burn3, burn4, burn5, burn6, burn7, burn8, burn9, burn10):
    cal_burned_result = int(burn1) + int(burn2) + int(burn3) + int(burn4) + int(burn5) + int(burn6) + int(burn7) + int(burn8) + int(burn9) + int(burn10)
    return cal_burned_result
def burner_counter(request):
    return render(request, "calorieking/burner_calculator.html")
@login_required(login_url='login')
def results(request):
    calorie_results = CalorieResult.objects.all().order_by('-id')
    macro_results = Macros.objects.all().order_by('-id')
    return render(request, "calorieking/results.html", {'calorie_results':calorie_results, 'macro_results':macro_results})
@login_required(login_url='login')
def burner_results(request):
    return render(request, "calorieking/burner_results.html")
def contact(request):
    return render(request, "calorieking/contact.html")