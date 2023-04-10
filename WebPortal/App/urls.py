from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signUp, name='signup'),
    path('addSlot', views.addSlot, name = 'addSlot'), 
    path('viewSlots', views.viewAvailableSlots, name = 'viewSlots' ), 
    # path('viewSlot/<int:pk>', views.viewSlot, name='viewSlot'),
    path('deleteSlot/<int:pk>', views.deleteSlot, name='deleteSlot'),
    path('updateSlot/<int:pk>', views.updateSlot, name='updateSlot'),
    path('bookSlot/<int:pk>', views.bookSlot, name='bookSlot'),
    path('unbookSlot/<int:pk>', views.unbookSlot, name='unbookSlot'),
    path('mySlots', views.mySlots, name='mySlots'), 
    path('requestCompletion/<int:pk>', views.requestCompletion, name='requestCompletion'),
    path('acceptRequest/<int:pk>', views.acceptRequest, name='acceptRequest'),
    path('declineRequest/<int:pk>', views.declineRequest, name='declineRequest'),
]


## Tasks for frontend
# label formatting in all forms
