# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Airlines(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'airlines'

class AirlinesRefTable(models.Model):
    unique_carrier_code = models.CharField(primary_key=True, max_length=11)
    airline_description = models.CharField(max_length=100)
    airline_id = models.ForeignKey(Airlines)
    class Meta:
        managed = True
        db_table = 'airlines_ref_table'

    def __unicode__(self):
		return '%s - %s' %(self.unique_carrier_code, self.airline_description)

class AirportsRefTable(models.Model):
    unique_airport_id = models.IntegerField(primary_key=True)
    airport_code = models.CharField(unique=True, max_length=3)
    airport_sequence = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=3)
    airport_name = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'airports_ref_table'
    def __unicode__(self):
		return '%s - %s' %(self.airport_code, self.airport_name)

class Allairports(models.Model):
    id = models.IntegerField(primary_key=True)
    totalflights = models.FloatField(db_column='totalFlights',blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    delrate = models.FloatField(db_column='delRate', blank=True, null=True) # Field name made lowercase.
    canrate = models.FloatField(db_column='canRate', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'allairports'

class Dephour(models.Model):
	hourid = models.IntegerField(db_column='hourID', unique=True, primary_key=True) # Field name made lowercase.
	depblock = models.CharField(db_column='DepBlock', max_length=45, blank=True) # Field name made lowercase.
	totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
	totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
	totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
	pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
	pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = True
		db_table = 'dephour'
	def __unicode__(self):
		return '%s' %(self.depblock)

class Destcity(models.Model):
    destid = models.IntegerField(db_column='DestID', primary_key=True) # Field name made lowercase.
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'destcity'

class Distance(models.Model):
    distid = models.IntegerField(db_column='distID', primary_key=True) # Field name made lowercase.
    distancegroup = models.IntegerField(db_column='distanceGroup', blank=True, null=True) # Field name made lowercase.
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'distance'

class Distgroups(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    originairportid = models.IntegerField(db_column='OriginAirportID', blank=True, null=True) # Field name made lowercase.
    destairportid = models.IntegerField(db_column='DestAirportID', blank=True, null=True) # Field name made lowercase.
    distancegroup = models.IntegerField(db_column='DistanceGroup', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'distgroups'

class Flights(models.Model):
    flights_id = models.IntegerField(primary_key=True)
    year = models.TextField(db_column='Year') # Field name made lowercase. This field type is a guess.
    quarter = models.IntegerField(db_column='Quarter', blank=True, null=True) # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True) # Field name made lowercase.
    dayofmonth = models.IntegerField(db_column='DayofMonth', blank=True, null=True) # Field name made lowercase.
    dayofweek = models.IntegerField(db_column='DayOfWeek', blank=True, null=True) # Field name made lowercase.
    flightdate = models.DateField(db_column='FlightDate', blank=True, null=True) # Field name made lowercase.
    uniquecarrier = models.CharField(db_column='UniqueCarrier', max_length=25, blank=True) # Field name made lowercase.
    airlineid = models.IntegerField(db_column='AirlineID', blank=True, null=True) # Field name made lowercase.
    carrier = models.CharField(db_column='Carrier', max_length=12, blank=True) # Field name made lowercase.
    tailnum = models.CharField(db_column='TailNum', max_length=12, blank=True) # Field name made lowercase.
    flightnum = models.IntegerField(db_column='FlightNum', blank=True, null=True) # Field name made lowercase.
    originairportid = models.IntegerField(db_column='OriginAirportID', blank=True, null=True) # Field name made lowercase.
    originairportseqid = models.IntegerField(db_column='OriginAirportSeqID', blank=True, null=True) # Field name made lowercase.
    origincitymarketid = models.IntegerField(db_column='OriginCityMarketID', blank=True, null=True) # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=12, blank=True) # Field name made lowercase.
    origincityname = models.CharField(db_column='OriginCityName', max_length=50, blank=True) # Field name made lowercase.
    originstate = models.CharField(db_column='OriginState', max_length=12, blank=True) # Field name made lowercase.
    originstatefips = models.IntegerField(db_column='OriginStateFips', blank=True, null=True) # Field name made lowercase.
    originstatename = models.CharField(db_column='OriginStateName', max_length=25, blank=True) # Field name made lowercase.
    originwac = models.IntegerField(db_column='OriginWac', blank=True, null=True) # Field name made lowercase.
    destairportid = models.IntegerField(db_column='DestAirportID', blank=True, null=True) # Field name made lowercase.
    destairportseqid = models.IntegerField(db_column='DestAirportSeqID', blank=True, null=True) # Field name made lowercase.
    destcitymarketid = models.IntegerField(db_column='DestCityMarketID', blank=True, null=True) # Field name made lowercase.
    dest = models.CharField(db_column='Dest', max_length=5, blank=True) # Field name made lowercase.
    destcityname = models.CharField(db_column='DestCityName', max_length=50, blank=True) # Field name made lowercase.
    deststate = models.CharField(db_column='DestState', max_length=12, blank=True) # Field name made lowercase.
    deststatefips = models.IntegerField(db_column='DestStateFips', blank=True, null=True) # Field name made lowercase.
    deststatename = models.CharField(db_column='DestStateName', max_length=25, blank=True) # Field name made lowercase.
    destwac = models.IntegerField(db_column='DestWac', blank=True, null=True) # Field name made lowercase.
    crsdeptime = models.IntegerField(db_column='CRSDepTime', blank=True, null=True) # Field name made lowercase.
    deptime = models.IntegerField(db_column='DepTime', blank=True, null=True) # Field name made lowercase.
    depdelay = models.IntegerField(db_column='DepDelay', blank=True, null=True) # Field name made lowercase.
    depdelayminutes = models.IntegerField(db_column='DepDelayMinutes', blank=True, null=True) # Field name made lowercase.
    depdel15 = models.IntegerField(db_column='DepDel15', blank=True, null=True) # Field name made lowercase.
    departuredelaygroups = models.IntegerField(db_column='DepartureDelayGroups', blank=True, null=True) # Field name made lowercase.
    deptimeblk = models.CharField(db_column='DepTimeBlk', max_length=12, blank=True) # Field name made lowercase.
    taxiout = models.IntegerField(db_column='TaxiOut', blank=True, null=True) # Field name made lowercase.
    wheelsoff = models.IntegerField(db_column='WheelsOff', blank=True, null=True) # Field name made lowercase.
    wheelson = models.IntegerField(db_column='WheelsOn', blank=True, null=True) # Field name made lowercase.
    taxiin = models.IntegerField(db_column='TaxiIn', blank=True, null=True) # Field name made lowercase.
    crsarrtime = models.IntegerField(db_column='CRSArrTime', blank=True, null=True) # Field name made lowercase.
    arrtime = models.IntegerField(db_column='ArrTime', blank=True, null=True) # Field name made lowercase.
    arrdelay = models.IntegerField(db_column='ArrDelay', blank=True, null=True) # Field name made lowercase.
    arrdelayminutes = models.IntegerField(db_column='ArrDelayMinutes', blank=True, null=True) # Field name made lowercase.
    arrdel15 = models.IntegerField(db_column='ArrDel15', blank=True, null=True) # Field name made lowercase.
    arrivaldelaygroups = models.IntegerField(db_column='ArrivalDelayGroups', blank=True, null=True) # Field name made lowercase.
    arrtimeblk = models.CharField(db_column='ArrTimeBlk', max_length=12, blank=True) # Field name made lowercase.
    cancelled = models.IntegerField(db_column='Cancelled', blank=True, null=True) # Field name made lowercase.
    cancellationcode = models.CharField(db_column='CancellationCode', max_length=25, blank=True) # Field name made lowercase.
    diverted = models.IntegerField(db_column='Diverted', blank=True, null=True) # Field name made lowercase.
    crselapsedtime = models.IntegerField(db_column='CRSElapsedTime', blank=True, null=True) # Field name made lowercase.
    actualelapsedtime = models.IntegerField(db_column='ActualElapsedTime', blank=True, null=True) # Field name made lowercase.
    airtime = models.IntegerField(db_column='AirTime', blank=True, null=True) # Field name made lowercase.
    flights = models.IntegerField(db_column='Flights', blank=True, null=True) # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance', blank=True, null=True) # Field name made lowercase.
    distancegroup = models.IntegerField(db_column='DistanceGroup', blank=True, null=True) # Field name made lowercase.
    carrier_delay = models.IntegerField(db_column='CarrierDelay', blank=True, null=True, default=0)
    weather_delay = models.IntegerField(db_column='WeatherDelay', blank=True, null=True, default=0)
    nas_delay = models.IntegerField(db_column='NasDelay', blank=True, null=True, default=0)
    weather_delay = models.IntegerField(db_column='WeatherDelay', blank=True, null=True, default=0)
    security_delay = models.IntegerField(db_column='SecurityDelay', blank=True, null=True, default=0)
    late_aircraft_delay = models.IntegerField(db_column='LateAircraftDelay', blank=True, null=True, default=0)
    class Meta:
        managed = True
        db_table = 'flights'

class Month(models.Model):
    monthid = models.IntegerField(db_column='monthID', unique=True, primary_key=True) # Field name made lowercase.
    monthName = models.CharField(db_column='monthName', null=True, blank=True, max_length=10)
    totaldays = models.IntegerField(blank=True,null=True)
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'month'
    def __unicode__(self):
		return '%s' %(self.monthName)

class Monthday(models.Model):
    monthday = models.IntegerField(db_column='monthDay', unique=True, primary_key=True) # Field name made lowercase.
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='PerTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'monthday'
    def __unicode__(self):
		return '%s' %(self.monthday)

class Origincity(models.Model):
    originid = models.IntegerField(db_column='OriginID', primary_key=True) # Field name made lowercase.
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'origincity'

class Weekday(models.Model):
    weekday = models.CharField(unique=True, max_length=1, primary_key=True)
    weekday_name = models.CharField(unique=True,max_length=10, null=True, blank=True)
    totalflights = models.FloatField(db_column='totalFlights', blank=True, null=True) # Field name made lowercase.
    totaldels = models.IntegerField(db_column='totalDels', blank=True, null=True) # Field name made lowercase.
    totalcans = models.IntegerField(db_column='totalCans', blank=True, null=True) # Field name made lowercase.
    pertotaldels = models.FloatField(db_column='perTotalDels', blank=True, null=True) # Field name made lowercase.
    pertotalcans = models.FloatField(db_column='perTotalCans', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'weekday'
    def __unicode__(self):
		return '%s' %(self.weekday_name)

class routes(models.Model):
    routeid = models.IntegerField(unique=True, primary_key=True)
    num_flights = models.IntegerField(default=0)
    origin_airport = models.IntegerField()
    dest_airport = models.IntegerField()
    airlineid = models.IntegerField()

class SavedSearches(models.Model):
    searchid = models.IntegerField(primary_key=True)
    search_name = models.CharField(max_length=30,default='N/A',null=False)
    userid = models.ForeignKey(User,null=False)
    origin_airport = models.ForeignKey(AirportsRefTable, related_name='origin',null=True)
    destination_airport = models.ForeignKey(AirportsRefTable, related_name='destination',null=True)
    airline = models.ForeignKey(AirlinesRefTable,null=True)
    dep_hour = models.ForeignKey(Dephour,null=True)
    month = models.ForeignKey(Month,null=True)
    month_day = models.ForeignKey(Monthday,null=True)
    weekday = models.ForeignKey(Weekday,null=True)

