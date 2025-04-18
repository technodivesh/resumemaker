from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel

class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    summary = models.TextField(help_text="Professional summary or objective", blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Education(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.school}"


class Experience(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Project(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ])

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


class Certification(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Language(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, choices=[
        ('Basic', 'Basic'),
        ('Conversational', 'Conversational'),
        ('Fluent', 'Fluent'),
        ('Native', 'Native')
    ])

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

class AwardAchievement(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='awards')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date_awarded = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class CustomSection(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='custom_sections')
    heading = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.heading
