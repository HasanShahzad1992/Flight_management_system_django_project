from django.db import models

class Passenger_Flight(models.Model):
    passenger_id=models.AutoField(primary_key=True)
    passenger_name=models.CharField(max_length=35)
    cnic=models.CharField(max_length=20)
    age=models.IntegerField()
class Flight(models.Model):
    flight_id=models.AutoField(primary_key=True)
    flight_number=models.CharField(max_length=15)
    destination=models.CharField(max_length=20)
class Passenger_Flight_Combined(models.Model):
    passenger_flight_id=models.AutoField(primary_key=True)
    passenger=models.ForeignKey(Passenger_Flight,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    date_flight=models.DateField()
class Airline_Login_Users(models.Model):
    airline_user_id=models.AutoField(primary_key=True)
    airline_user_email=models.EmailField(unique=True)
    airline_user_name=models.CharField(max_length=30)
    airline_user_password=models.CharField(max_length=30)
    airline_user_type=models.CharField(max_length=30)
    profile_picture=models.ImageField(upload_to="profile_pics",default=True)
