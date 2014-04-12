from django.shortcuts import render, redirect
from django.http import HttpResponse as response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.models import User
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import InputForm, UserCreationForm, AuthenticationForm, SaveSearchForm
from .models import Airlines, AirlinesRefTable, AirportsRefTable, Allairports, routes, Dephour, Destcity, Origincity, Distance, Distgroups, Month, Monthday, Weekday, SavedSearches

def bayes(request, origin=None, destination = None, airline = None, block = None, mon = None, md = None, w = None):
    all = Allairports.objects.all()

    if origin:
        ori = Origincity.objects.filter(originid=origin)
        dep = AirportsRefTable.objects.filter(unique_airport_id = origin)[0]
        depart = [ori[0].totalflights, ori[0].pertotaldels, ori[0].pertotalcans]
    else:
        dep = None
        depart = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if destination:
        de = Destcity.objects.filter(destid=destination)
        arrive = AirportsRefTable.objects.filter(unique_airport_id = destination)[0]
        dest = [de[0].totalflights, de[0].pertotaldels, de[0].pertotalcans]
    else:
        arrive = None
        dest = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if airline:
        car = Airlines.objects.filter(id=AirlinesRefTable.objects.filter(unique_carrier_code=airline)[0].airline_id_id)
        carrier = AirlinesRefTable.objects.filter(unique_carrier_code=airline)[0]
        air = [car[0].totalflights, car[0].pertotaldels, car[0].pertotalcans]
    else:
        carrier = None
        air = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if block:
        time = Dephour.objects.filter(hourid=block)[0]
        tblock =[time.totalflights, time.pertotaldels, time.pertotalcans]
    else:
        time= None
        tblock = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if mon:
        m = Month.objects.filter(monthid=mon)[0]
        month = [m.totalflights, m.pertotaldels, m.pertotalcans]
    else:
        m = None
        month = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if md:
        m_day = Monthday.objects.filter(monthday=md)[0]
        month_day = [m_day.totalflights, m_day.pertotaldels, m_day.pertotalcans]
    else:
        m_day = None
        month_day = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if w:
        w_day = Weekday.objects.filter(weekday=w)[0]
        week_day = [w_day.totalflights, w_day.pertotaldels, w_day.pertotalcans]
    else:
        w_day = None
        week_day = [all[0].totalflights, 1,1] #set % of all delays and cans to 1 and % of all flights to 1

    if origin and destination:
        # get distance group matching origin and destination airports
        dist_group = Distgroups.objects.filter(originairportid = origin, destairportid = destination)
        distance = Distance.objects.filter(distancegroup = dist_group[0].distancegroup)
        dist = [distance[0].totalflights, distance[0].pertotaldels, distance[0].pertotalcans]
    else:
        dist = [all[0].totalflights, 1,1]

    denom = ((depart[0]/all[0].totalflights) * (dest[0]/all[0].totalflights) * (air[0]/all[0].totalflights)*(tblock[0]/all[0].totalflights) * \
        (month[0]/all[0].totalflights) * (month_day[0]/all[0].totalflights) * (week_day[0]/all[0].totalflights) * dist[0]/all[0].totalflights)

    del_likelihood = str(100*(depart[1] * dest[1] * air[1] * tblock[1] * month[1] * month_day[1] * week_day[1] * dist[1] * all[0].delrate)/denom)[:5]
    can_likelihood = str(100*(depart[2] * dest[2] * air[2] * tblock[2] * month[2] * month_day[2] * week_day[2] * dist[1] * all[0].canrate)/denom)[:5]

    all_del_rate, all_can_rate = str(all[0].delrate*100)[:5], str(all[0].canrate*100)[:5]

    form2 = SaveSearchForm()
    context = {'del_likelihood':del_likelihood,'can_likelihood':can_likelihood,'all_del_rate':all_del_rate, 'all_can_rate':all_can_rate, \
                'origin':dep,'destination':arrive,'airline':carrier,'time':time,'m':m,'m_day':m_day,'w_day':w_day,'form2':form2}

    return context

def home(request):
    if request.method == 'POST': # If the form has been submitted...
        form = InputForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #call bayes calcs
            origin = request.POST.get('origin_airport_1')
            destination = request.POST.get('destination_airport_1')
            airline = request.POST.get('airline')
            block = request.POST.get('dep_hour')
            mon = request.POST.get('month')
            md = request.POST.get('monthday')
            w = request.POST.get('weekday')

            if request.user.is_authenticated():
                user_id = request.user.id
                request.session['user_id'] = user_id

            #capture request input for display in template
            request.session['flag'] = 'true'
            request.session['origin'] = origin
            request.session['destination'] = destination
            request.session['airline'] = airline
            request.session['block'] = block
            request.session['mon'] = mon
            request.session['md'] = md
            request.session['w'] = w

            if mon and md:
                d = datetime.date(2014,int(mon),int(md))
                now = datetime.datetime.now()
                if now.month > d.month:
                    dt_year = 2015
                else: dt_year = 2014
                dt = datetime.date(int(dt_year),int(mon),int(md))
                w = dt.weekday() + 1

            context = bayes(request, origin=origin, destination=destination, airline=airline, block=block, mon=mon, md=md, w=w)

            return render(request, 'flights/results.html', context)
    else:
        form = InputForm()

    return render(request,'flights/Home.html',{'form':form,})

def saveSearchToDB(request, search_name=None):
    user = User.objects.get(id=request.user.id)
    if search_name:
        name = search_name
    else:
        name = request.POST['search_name']

    ori = request.session['origin']
    if ori == '': origin = None
    else: origin = AirportsRefTable.objects.get(unique_airport_id=ori)

    dest = request.session['destination']
    if dest == '': destination = None
    else: destination = AirportsRefTable.objects.get(unique_airport_id=dest)

    air = request.session['airline']
    if air == '': airline = None
    else: airline = AirlinesRefTable.objects.get(unique_carrier_code=air)

    time = request.session['block']
    if time == '': block = None
    else: block = Dephour.objects.get(hourid=time)

    mont = request.session['mon']
    if mont == '': mon = None
    else: mon = Month.objects.get(monthid = mont)

    day = request.session['md']
    if day == '': md = None
    else: md = Monthday.objects.get(monthday = day)

    week = request.session['w']
    if week == '': w = None
    else: w = Weekday.objects.get(weekday=week)

    search = SavedSearches(search_name=name,origin_airport=origin, destination_airport=destination, \
    airline=airline, dep_hour=block, month=mon, month_day=md, weekday=w,userid=user)
    search.save()

def saveSearch(request):
    if request.method == 'POST':
        form = SaveSearchForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                saveSearchToDB(request)
                return HttpResponseRedirect("/searches")
            else:
                request.session['search_name'] = request.POST['search_name']
                return HttpResponseRedirect("/login")
    return render(request,'flights/searches.html',{'form':form,})

def searches(request):
    if request.user.id:
        results = []
        for s in SavedSearches.objects.filter(userid=request.user.id):
            context = bayes(request, origin=s.origin_airport_id, destination=s.destination_airport_id, airline=s.airline_id, block=s.dep_hour_id, \
                mon=s.month_id, md=s.month_day_id, w=s.weekday_id)
            results.append([context['del_likelihood'], context['can_likelihood'], \
                context['all_del_rate'], context['all_can_rate'], s.search_name, s.origin_airport, s.destination_airport, s.airline, \
                s.month, s.month_day, s.weekday, s.dep_hour])
        paginator = Paginator(results, 10)
        page = request.GET.get('page')
        try:
            searches = paginator.page(page)
        except PageNotAnInteger:
             searches = paginator.page(1)
        except EmptyPage:
            searches = paginator.page(paginator.num_pages)
        return render(request,'flights/searches.html',{'searches':searches})
    else:
        return HttpResponseRedirect("/login")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            user_login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "flights/register.html", {'form': form,})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(None, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            user_login(request, user)
            if request.session.get('search_name'):
                saveSearchToDB(request, search_name=request.session.get('search_name'))
                return HttpResponseRedirect("/searches")
            else:
                return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "flights/login.html", {'form': form,})

def about(request):
    return render(request, "flights/about.html")

