from django.http import JsonResponse
from django.contrib.auth import authenticate
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@csrf_exempt
def signup(req):
    if req.method == "POST":
        data = json.loads(req.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({"message": "User created successfully"}, status=201)
    
@csrf_exempt
def login_(req):
    if req.method=='POST':
        data=json.loads(req.body)
        username=data['username']
        password=data['password']
        user =authenticate(username=username,password=password)
        if user is None:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
        refresh = RefreshToken.for_user(user)
        print(refresh)
        return JsonResponse({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
        
        return JsonResponse