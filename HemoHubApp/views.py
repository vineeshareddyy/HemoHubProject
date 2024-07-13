# views.py

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Notification, PersonData
from .resources import PersonDataResource
from django.contrib import messages
from tablib import Dataset
import csv, io
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def upload(request):
    if request.method == "POST":
        persondata_resource = PersonDataResource()
        dataset = Dataset()
        new_persondata = request.FILES['myfile']

        if not new_persondata.name.endswith('csv'):
            messages.error(request, 'Please upload a CSV file only')
            return render(request, 'home.html')

        data_set = new_persondata.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            PersonData.objects.update_or_create(
                Person_Name=column[0],
                Blood_Type=column[1],
                Component=column[2],
                Quantity=column[3],
                Expiry_Date=column[4]
            )
        messages.success(request, 'File successfully uploaded')

    return render(request, 'home.html')
def reject_notification(request, notification_id):
    messages.success(request, 'Notification rejected.')
    # Redirect to the appropriate dashboard based on the user's company
    if request.user.username == 'redcross':
        return redirect('redcross_dashboard')
    elif request.user.username == 'Medwin':
        return redirect('company2_dashboard')
    elif request.user.username == 'Ozone':
        return redirect('company1_dashboard')
    else:
        messages.error(request, 'Unauthorized access')
       
       

def redcross_dashboard(request):
    notifications = Notification.objects.filter(is_read=False)  # Fetch unread notifications
    return render(request, 'redcross_dashboard.html', {'notifications': notifications})

def dummy_dashboard(request):
    notifications = Notification.objects.filter(is_read=False)  # Fetch unread notifications
    return render(request, 'dummy_dashboard.html', {'notifications': notifications})

def accept_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.delete()
    messages.success(request, 'Notification accepted and removed.')

    # Redirect to the appropriate dashboard based on the user's company
    if request.user.username == 'redcross':
        return redirect('redcross_dashboard')
    elif request.user.username == 'Medwin':
        return redirect('company2_dashboard')
    elif request.user.username == 'Ozone':
        return redirect('company1_dashboard')
    else:
        messages.error(request, 'Unauthorized access')
        return redirect('company_login')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Your account has been created successfully.')
        return redirect('login_view')

    return render(request, 'signup.html')


def redcross(request):
    return render(request, 'redcross.html')

def redcross_donors_list(request):
    return render(request, 'redcross_donors_list.html')

def redcross_blood_stock(request):
    return render(request, 'redcross_blood_stock.html')

def redcross_donor_registration(request):
    return render(request, 'redcross_donor_registration.html')

def redcross_request_blood(request):
    return render(request, 'redcross_request_blood.html')

def redcross_blood_donation_camps(request):
    return render(request, 'redcross_blood_donation_camps.html')

def redcross_about(request):
    return render(request, 'redcross_about.html')

def redcross_contact(request):
    return render(request, 'redcross_contact.html')

def redcross_profile(request):
    return render(request, 'redcross_profile.html')

def redcross_logout(request):
    return render(request, 'redcross_logout.html')


# Add new dashboard views
def company1_dashboard(request):
    notifications = Notification.objects.filter(is_read=False)  # Fetch unread notifications
    return render(request, 'company1_dashboard.html', {'notifications': notifications})

def company2_dashboard(request):
    notifications = Notification.objects.filter(is_read=False)  # Fetch unread notifications
    return render(request, 'company2_dashboard.html', {'notifications': notifications})


# Add new pages for Company 1
def company1_donors_list(request):
    return render(request, 'company1_donors_list.html')

def company1_blood_stock(request):
    return render(request, 'company1_blood_stock.html')

def company1_donor_registration(request):
    return render(request, 'company1_donor_registration.html')

def company1_request_blood(request):
    return render(request, 'company1_request_blood.html')

def company1_blood_donation_camps(request):
    return render(request, 'company1_blood_donation_camps.html')

def company1_about(request):
    return render(request, 'company1_about.html')

def company1_contact(request):
    return render(request, 'company1_contact.html')

def company1_profile(request):
    return render(request, 'company1_profile.html')

def company1_logout(request):
    return render(request, 'company1_logout.html')


# Add new pages for Company 2
def company2_donors_list(request):
    return render(request, 'company2_donors_list.html')

def company2_blood_stock(request):
    return render(request, 'company2_blood_stock.html')

def company2_donor_registration(request):
    return render(request, 'company2_donor_registration.html')

def company2_request_blood(request):
    return render(request, 'company2_request_blood.html')

def company2_blood_donation_camps(request):
    return render(request, 'company2_blood_donation_camps.html')

def company2_about(request):
    return render(request, 'company2_about.html')

def company2_contact(request):
    return render(request, 'company2_contact.html')

def company2_profile(request):
    return render(request, 'company2_profile.html')

def company2_logout(request):
    return render(request, 'company2_logout.html')


def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on the username of the logged-in user
            if user.username == 'redcross':
                return redirect('redcross_dashboard')
            elif user.username == 'Medwin':
                return redirect('company2_dashboard')
            elif user.username == 'Ozone':
                return redirect('company1_dashboard')
            else:
                messages.error(request, 'Invalid credentials or unauthorized access')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'company_login.html')

# Add new about views
def company1_about(request):
    return render(request, 'company1_about.html')

def company2_about(request):
    return render(request, 'company2_about.html')


