from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tradeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trade/', views.tradeList.as_view()),
]
