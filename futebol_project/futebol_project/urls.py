from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from core.api_views import TimeViewSet, JogadorViewSet, PartidaViewSet

# 🔹 Router da API
router = DefaultRouter()
router.register(r'times', TimeViewSet)
router.register(r'jogadores', JogadorViewSet)
router.register(r'partidas', PartidaViewSet)

# 🔹 URLs principais
urlpatterns = [
    path('admin/', admin.site.urls),

    # Web
    path('', include('core.urls')),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # API
    path('api/', include(router.urls)),
]