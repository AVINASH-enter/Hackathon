from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm
def index(request):
    return render(request,'eventapp/index.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'eventapp/events.html',dict_eve)




# View for booking the event
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


def book_event(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the booking and get the booking instance
            return redirect('booking_success', booking_id=booking.id)  # Pass the booking_id to the success page
    else:
        form = BookingForm()

    return render(request, 'eventapp/book_event.html', {'form': form})


# View for displaying the booking success page
from django.shortcuts import render, get_object_or_404
from .models import Booking

def booking_success(request, booking_id):
    # Fetch the booking instance using booking_id
    booking = get_object_or_404(Booking, id=booking_id)  # Handle the case where the booking does not exist
    return render(request, 'eventapp/booking_success.html', {'booking': booking})




# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page
    else:
        form = ContactForm()

    return render(request, 'eventapp/contact.html', {'form': form})


def about(request):
    return render(request,'eventapp/about.html')


# views.py

from django.shortcuts import render, redirect
from .forms import UserProfileForm


def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a profile page or any other page
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'eventapp/linkedin.html', {'form': form})


from django.shortcuts import render
from django.http import HttpResponse

def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        event = request.POST.get("event")
        message = request.POST.get("message")

        # Save or process the feedback
        # Example: Save to a database or send an email
        print(f"Feedback Received: {name}, {email}, {event}, {message}")

        return render(request, "eventapp/thank_you.html")
    return render(request, "eventapp/feedback.html")

