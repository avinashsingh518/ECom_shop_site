from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),         #rout for jwt token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),        #rout for jwt token

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

