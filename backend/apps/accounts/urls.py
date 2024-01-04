from django.urls import include, path

app_name = "accounts"
urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration", include("dj_rest_auth.registration.urls")),
]
