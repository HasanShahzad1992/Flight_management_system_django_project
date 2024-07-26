from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from flight_app import models

def load_passenger_flight_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
    return render(initial_request_from_front_end,"load_add_passenger_flight.html",{"username":username})
@csrf_exempt
def add_passenger_flight_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        passenger_s_name=initial_request_from_front_end.POST.get("name of passenger")
        passenger_s_cnic=initial_request_from_front_end.POST.get("cnic of customer")
        passenger_s_age=initial_request_from_front_end.POST.get("age of customer")
        passenger_add_object=models.Passenger_Flight.objects.create(passenger_name=passenger_s_name,cnic=passenger_s_cnic,age=passenger_s_age)
        return render(initial_request_from_front_end,"load_add_passenger_flight.html",{"passenger_add":"passenger flight successfully added","username":username})
def view_all_passenger_flight_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_passenger_flight_objects=models.Passenger_Flight.objects.all()
        return render(initial_request_from_front_end,"view_all_passenger_of_flights.html",{"all_passenger_flight":all_passenger_flight_objects,"username":username})
def load_update_passenger_flight_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
      username=initial_request_from_front_end.session["username"]
      all_passenger_flight_objects=models.Passenger_Flight.objects.all()
      return render(initial_request_from_front_end,"load_update_passenger_flight.html",{"all_passenger_flight":all_passenger_flight_objects,"username":username})
@csrf_exempt
def update_passenger_flight_html(initial_request_from_front_end,passenger_update_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_passenger_flight_objects = models.Passenger_Flight.objects.all()
        particular_passenger_flight_object=models.Passenger_Flight.objects.get(passenger_id=passenger_update_id)
        passenger_s_name=initial_request_from_front_end.POST.get("name_of_passenger")
        passenger_s_cnic=initial_request_from_front_end.POST.get("age_of_passenger")
        passenger_s_age=initial_request_from_front_end.POST.get("cnic_of_passenger")
        particular_passenger_flight_object.passenger_name=passenger_s_name
        particular_passenger_flight_object.cnic=passenger_s_cnic
        particular_passenger_flight_object.age=passenger_s_age
        particular_passenger_flight_object.save()
        return render(initial_request_from_front_end,"load_update_passenger_flight.html",{"all_passenger_flight":all_passenger_flight_objects,"message":"passenger_updated","username":username})
def load_passenger_flight_delete_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_passenger_objects=models.Passenger_Flight.objects.all()
        return render(initial_request_from_front_end,"load_delete_passenger_flight.html",{"all_passenger":all_passenger_objects,"username":username})
@csrf_exempt
def delete_passenger_flight_html(initial_request_from_front_end,delete_passenger_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_passenger_objects=models.Passenger_Flight.objects.all()
        particular_passenger_object=models.Passenger_Flight.objects.get(passenger_id=delete_passenger_id)
        particular_passenger_object.delete()
        return render(initial_request_from_front_end,"load_delete_passenger_flight.html",{"all_passenger":all_passenger_objects,"message":"deleted_successfully","username":username})


def load_flight_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_add_flights.html",{"username":username})
@csrf_exempt
def add_flight_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        number_of_flight=initial_request_from_front_end.POST.get("flight_number")
        destination_of_flight=initial_request_from_front_end.POST.get("destination of flight")
        models.Flight.objects.create(flight_number=number_of_flight,destination=destination_of_flight)
        return render(initial_request_from_front_end,"load_add_flights.html",{"message":"successfully_added","username":username})
def view_all_flights_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_flights_objects=models.Flight.objects.all()
        return render(initial_request_from_front_end,"view_all_flights.html",{"all_flights":all_flights_objects,"username":username})
def load_flights_update_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_flight_objects=models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_flights_update.html",{"all_flight":all_flight_objects,"username":username})
@csrf_exempt
def update_flights_html(initial_request_from_front_end,flight_update_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        particular_update_flight_object=models.Flight.objects.get(flight_id=flight_update_id)
        flight_s_number=initial_request_from_front_end.POST.get("new_flight_number")
        flight_s_destination=initial_request_from_front_end.POST.get("new_destination")
        particular_update_flight_object.flight_number=flight_s_number
        particular_update_flight_object.destination=flight_s_destination
        particular_update_flight_object.save()
        all_flight_objects = models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_flights_update.html",{"all_flight":all_flight_objects,"message":"updated_successfully","username":username})
def load_flights_delete_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_flight_objects=models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_delete_flights.html",{"all_flights":all_flight_objects,"username":username})
@csrf_exempt
def delete_flights_html(initial_reqest_from_front_end,flight_delete_id):
    if initial_reqest_from_front_end.method=="POST":
        username=initial_reqest_from_front_end.session["username"]
        all_flight_objects = models.Flight.objects.all()
        particular_flight_object=models.Flight.objects.get(flight_id=flight_delete_id)
        particular_flight_object.delete()
        return render(initial_reqest_from_front_end,"load_delete_flights.html",{"all_flights":all_flight_objects,"message":"deleted_successfully","username":username})

def load_passenger_flight_combined_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_passenger_objects=models.Passenger_Flight.objects.all()
        all_flight_objects=models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_add_passenger_flight_combined.html",{"all_passenger":all_passenger_objects,"all_flights":all_flight_objects,"username":username})
@csrf_exempt
def add_passenger_flight_combined_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        passenger_s_id=initial_request_from_front_end.POST.get("passenger_s_id")
        flight_id=initial_request_from_front_end.POST.get("flight_s_id")
        date_flight=initial_request_from_front_end.POST.get("date select for travelling")
        passenger_flight_combined_object=models.Passenger_Flight_Combined.objects.create(passenger_id=passenger_s_id,flight_id=flight_id,date_flight=date_flight)
        all_passenger_objects = models.Passenger_Flight.objects.all()
        all_flight_objects = models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_add_passenger_flight_combined.html",{"all_passenger":all_passenger_objects,"all_flights":all_flight_objects,"message":"added_successfully","username":username})
def view_all_passenger_flight_combined_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_passenger_flight_combined_objects = models.Passenger_Flight_Combined.objects.all()
        return render(initial_request_from_front_end,"view_all_passenger_flight_combined.html",{"all_passenger_flight_combined":all_passenger_flight_combined_objects,"username":username})
def load_passenger_flight_combined_update(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        passenger_flight_combined_objects=models.Passenger_Flight_Combined.objects.all()
        all_passenger_objects=models.Passenger_Flight.objects.all()
        all_flight_objects=models.Flight.objects.all()
        return render(initial_request_from_front_end,"load_passenger_flight_combined_update.html",{"passenger_flight_combined":passenger_flight_combined_objects,"all_passenger":all_passenger_objects,"all_flights":all_flight_objects,"username":username})

@csrf_exempt
def update_passenger_flight_combined(initial_request_from_front_end,passenger_flight_combined_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        passenger_flight_combined_objects = models.Passenger_Flight_Combined.objects.all()
        all_passenger_objects = models.Passenger_Flight.objects.all()
        all_flight_objects = models.Flight.objects.all()
        new_passenger_id=initial_request_from_front_end.POST.get("passenger_id_to_be_updated")
        new_flight_id=initial_request_from_front_end.POST.get("flight_id_to_be_updated")
        new_date_flight=initial_request_from_front_end.POST.get("date_of_flight_to_be_updated")
        particular_passenger_flight_combined_object=models.Passenger_Flight_Combined.objects.get(passenger_flight_id=passenger_flight_combined_id)
        particular_passenger_flight_combined_object.passenger_id=new_passenger_id
        particular_passenger_flight_combined_object.flight_id=new_flight_id
        particular_passenger_flight_combined_object.date_flight=new_date_flight
        particular_passenger_flight_combined_object.save()
        return render(initial_request_from_front_end,"load_passenger_flight_combined_update.html",{"passenger_flight_combined":passenger_flight_combined_objects,"all_passenger":all_passenger_objects,"all_flights":all_flight_objects,"message":"updated_successfully","username":username})

def load_passenger_flight_combined_delete_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_passenger_flight_combined_objects=models.Passenger_Flight_Combined.objects.all()
        return render(initial_request_from_front_end,"load_delete_passenger_flight_combined.html",{"all_passenger_flight_combined":all_passenger_flight_combined_objects,"username":username})
@csrf_exempt
def delete_passenger_flight_combined_html(initial_request_from_front_end,delete_flight_combined_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_passenger_flight_combined_objects = models.Passenger_Flight_Combined.objects.all()
        particular_flight_object_object=models.Passenger_Flight_Combined.objects.get(passenger_flight_id=delete_flight_combined_id)
        particular_flight_object_object.delete()
        return render(initial_request_from_front_end,"load_delete_passenger_flight_combined.html",{"all_passenger_flight_combined":all_passenger_flight_combined_objects,"message":"deleted_successfully","username":username})

def load_flight_system_signup(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            if usertype=="entry":
                return redirect("load_entry_flight_system_home")
            elif usertype=="admin":
                return redirect("load_admin_flight_system_home")
        except:
            return render(initial_request_from_front_end,"load_signup_flight_system.html")
def signup_flight_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
            email_user=initial_request_from_front_end.POST.get("email_chosen_by_user")
            user_name_user=initial_request_from_front_end.POST.get("user_name_chosen_by_user")
            password_user=initial_request_from_front_end.POST.get("password_chosen_by_user")
            particular_flight_system_object=models.Airline_Login_Users.objects.create(airline_user_email=email_user,airline_user_name=user_name_user,airline_user_password=password_user,airline_user_type="admin")
            particular_flight_system_object.save()
            return render(initial_request_from_front_end,"load_signup_flight_system.html",{"message":"sign_up successful"})
def load_flight_system_login(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            if usertype=="admin":
                return redirect("load_admin_flight_system_home")
            elif usertype=="entry":
                return redirect("load_entry_flight_system_home")
        except:
            return render(initial_request_from_front_end,"load_login_flight_system.html")
def login_flight_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email_user=initial_request_from_front_end.POST.get("email_written_by_user")
        password_user=initial_request_from_front_end.POST.get("password_written_by_user")
        try:
            particular_login_object=models.Airline_Login_Users.objects.get(airline_user_email=email_user,airline_user_password=password_user)
            initial_request_from_front_end.session["username"]=particular_login_object.airline_user_name
            initial_request_from_front_end.session["usertype"]=particular_login_object.airline_user_type
            initial_request_from_front_end.session["userid"]=particular_login_object.airline_user_id
            if "admin"==initial_request_from_front_end.session["usertype"]:
                return redirect("load_admin_flight_system_home")
            elif "entry"==initial_request_from_front_end.session["usertype"]:
                return redirect("load_entry_flight_system_home")
        except:
            return render(initial_request_from_front_end,"load_login_flight_system.html",{"message":"wrong password or email"})
def load_entry_flight_system_home(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name_variable=initial_request_from_front_end.session["username"]
            user_type_variable=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            if user_type_variable=="entry":
                return render(initial_request_from_front_end,"load_entry_home_flight_system.html",{"user_name":user_name_variable,"userid":userid})
            else:
                return redirect("load_admin_flight_system_home")
        except:
            return redirect("load_flight_system_login")
def load_admin_flight_system_home(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            user_name_variable=initial_request_from_front_end.session["username"]
            user_type_variable=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            if user_type_variable=="admin":
                return render(initial_request_from_front_end,"load_admin_home_flight_system.html",{"username":user_name_variable,"userid":userid})
            else:
                return redirect("load_entry_flight_system_home")
        except:
            return redirect("load_flight_system_login")

def logout_flight_system(initial_request_from_front_end):
    initial_request_from_front_end.session.flush()
    return redirect("load_flight_system_login")

def upload_image(initial_request_from_front_end,userid):
    if initial_request_from_front_end.method=="POST":
        picture_uploaded=initial_request_from_front_end.FILES.get("profile_picture")
        particular_picture_object=models.Airline_Login_Users.objects.get(airline_user_id=userid)
        particular_picture_object.profile_picture=picture_uploaded
        particular_picture_object.save()
        if "admin"==initial_request_from_front_end.session["usertype"]:
            return redirect("load_admin_flight_system_home")
        elif "entry"==initial_request_from_front_end.session["usertype"]:
            return redirect("load_entry_flight_system_home")
















