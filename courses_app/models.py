from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['name']) < 4:
            errors['name'] = "Course name is too short"
        if len(reqPOST['description']) < 10:
            errors['description'] = "Description is too short"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()