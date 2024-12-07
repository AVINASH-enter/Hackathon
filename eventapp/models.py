from django.db import models

class Event(models.Model):
    img = models.ImageField(upload_to="pic")  # Image upload
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# models.py
class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=10)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to Event
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)  # Automatically sets booked on date

    def __str__(self):
        return f"{self.cus_name} - {self.name.name}"  # Access Event's name through the ForeignKey




# models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.created_at}'

# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    from django.db import models

    class Feedback(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.name} - {self.email}"

