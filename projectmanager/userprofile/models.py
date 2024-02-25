from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

ROLE_CHOICES = (
    ('admin', 'แอดมิน'),
    ('student', 'นักเรียน'),
    ('teacher', 'อาจารย์'),
)

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    phone = models.CharField(max_length=10, blank=True)
    role = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

class Qualification(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name 
class Year(models.Model):
    year = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.year)

class Room(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.qualification.name + ' ' + self.department.name + ' ' + str(self.year.year) + ' ' + self.room.name

class ProfileStudent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True)
    student_id = models.CharField(max_length=9, blank=True) #รหัสนักเรียน
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True) #กลุ่ม
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.user.username