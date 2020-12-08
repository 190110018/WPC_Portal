from django.urls import path

from . import views

urlpatterns = [
    path('instructions/', views.instructions, name="instructions"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('problems/',views.Problem,name="problems"),
    path('upload/',views.upload_file,name="file_upload")
]
