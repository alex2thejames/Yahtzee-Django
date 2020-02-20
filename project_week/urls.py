from django.urls import path, include

urlpatterns = [
    path('', include('yahtzee_app.urls')),
]
