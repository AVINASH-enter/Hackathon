from django import forms
from .models import Booking

# Custom DateInput widget to display a calendar date picker
class DateInput(forms.DateInput):
    input_type = 'date'  # HTML5 input type for date picker

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields in the form

        # Apply the DateInput widget to the booking_date field to use a calendar picker
        widgets = {
            'booking_date': DateInput(attrs={'class': 'form-control'}),  # Calendar input for date
            'cus_name': forms.TextInput(attrs={'class': 'form-control'}),  # Styling for customer name
            'cus_ph': forms.TextInput(attrs={'class': 'form-control'}),    # Styling for customer phone
            'name': forms.Select(attrs={'class': 'form-control'}),         # Dropdown for Event ForeignKey
        }

        # Custom labels for form fields
        labels = {
            'cus_name': "Customer Name:",
            'cus_ph': "Customer Phone:",
            'name': "Event Name:",
            'booking_date': "Booking Date:",
        }

# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

# forms.py

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['linkedin_url']
