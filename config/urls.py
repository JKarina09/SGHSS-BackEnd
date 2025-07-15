
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas da API JWT
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rotas da aplicação gestao
    path('', include('gestao.urls')),  # <- necessário para reconhecer /login/

    # Redirecionamento da raiz para a tela de login
    path('', RedirectView.as_view(url='/login/', permanent=False)),
]
