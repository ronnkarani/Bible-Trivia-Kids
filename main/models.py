from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def is_admin(self):
        return self.role == "admin"

    def is_parent(self):
        return self.role == "parent"

    def is_student(self):
        return self.role == "student"


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children', limit_choices_to={'role': 'parent'})
    
    age = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
