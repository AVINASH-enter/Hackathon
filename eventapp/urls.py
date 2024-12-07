from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.events,name='events'),
    path('book_event',views.book_event,name='book_event'),
    path('booking_success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('feedback/', views.feedback_view, name='feedback')

]