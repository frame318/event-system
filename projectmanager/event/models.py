from django.db import models
from django.urls import reverse
from userprofile.models import ProfileStudent, Department, Year
import uuid
# Create your models here.

EVENT_TYPE_CHOICES = (
    ('academic', 'กิจกรรมทางวิชาการ'),
    ('non-academic', 'กิจกรรมทางนอกหลักสูตร'),
    ('social', 'กิจกรรมทางสังคม'),
)
    
class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to='event_images', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES, blank=True)
    credit = models.IntegerField(default=0)
    number_required_participants = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

class ApplyEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(ProfileStudent, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.event.title} - {self.student.user.username}'

class EventParticipation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    apply_event = models.ForeignKey(ApplyEvent, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    checkin = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.apply_event.event.title} - {self.apply_event.student.user.username}'