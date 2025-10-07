from django.shortcuts import render, redirect
from django.http import HttpResponse
from supabase import create_client
from django.conf import settings

# connect to Supabase
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def home(request):
    return HttpResponse("Welcome to the User Registration App!")  # Simple home page
    

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = {
            'username': username,
            'email': email,
            'password': password,
        }

        # insert into Supabase
        response = supabase.table('User').insert(data).execute()

        if response.data:
            return HttpResponse("Registration successful!")
        else:
            return HttpResponse("Error: could not register user.")

    return render(request, 'accounts/register.html')
    
    

def login_view(request):

        context = {}  # Holds messages for the template

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            # Query Supabase for the user
            response = supabase.table("User").select("*").eq("username", username).execute()
            data = response.data
            
            if data:  # User found
                if data[0]["password"] == password:
                    context["success"] = f"Login successful! Welcome, {username}."
                else:
                    context["error"] = "Incorrect password. Please try again."
            else:  # User not found
                context["error"] = "Username not found. Please try again."

        return render(request, "accounts/login.html", context)
        
