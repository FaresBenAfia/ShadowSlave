# backend/ShadowSlave/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from .views import RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the ShadowSlave API!")

# Main URL configuration for the entire project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL mapped to home view
    path('api/characters/', include('app.characters.urls')),  # Correct include for characters app
    path('api/shadowslave/', include('app.shadowslave.urls')),  # Correct include for shadowslave app
     path('', ShadowslaveView.as_view(), name='shadowslave-view'),
     path('register/', RegisterUser.as_view(), name='register'),
     path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
