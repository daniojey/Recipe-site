from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('logout/', views.logout, name="logout"),
    # path('profile/', views.RecipesPageView.as_view(), name='profile'),
    # path('profile/my-recipe/', views.RecipesPageView.as_view(), name='my_recipe'),
    
]
