from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/cookie-stands/", include("cookie_stands.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
