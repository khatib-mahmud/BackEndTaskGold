
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('mobile_list/',views.mobile_list,name='mobile_list'),
    path('addmobile/',views.addmobile,name='addmobile'),
    path("mobiledelete/<int:id>/", views.mobiledelete, name="mobiledelete"),
    path("mobileinfo/<int:id>/", views.mobileinfo, name="mobileinfo")
]
