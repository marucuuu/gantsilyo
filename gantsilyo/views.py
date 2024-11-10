from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdminUserCreationForm
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate, login

# ADMIN VIEW START

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def admin_adduser(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = "Admin" if user.is_superuser else "Employee"
            messages.success(request, f"{role} user '{user.username}' added successfully.")
            return redirect('admin_adduser')  # Redirect to a relevant page
        else:
            messages.error(request, "Error adding user. Please check the form.")
    else:
        form = AdminUserCreationForm()
    
    return render(request, 'admin/admin_adduser.html', {'form': form})


def admin_addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('admin_addproduct')
        else:
            messages.error(request, "Error adding product. Please check the form.")
    else:
        form = ProductForm()
    
    return render(request, 'admin/admin_addproduct.html', {'form': form})



# ADMIN VIEW END






# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Assuming this is your URL pattern for the admin dashboard
            else:
                return redirect('some_other_dashboard')  # Redirect regular users to their dashboard
        else:
            # Handle invalid login attempt
            return render(request, 'login/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login/login.html')

def home(request):
    return render(request, 'home/home.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'home/product.html', {'products': products})

def about(request):
    return render(request, 'home/about.html')