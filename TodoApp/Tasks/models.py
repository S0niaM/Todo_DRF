from django.db import models

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    urgent =models.BooleanField(default=False)

    def __str__(self):
        return self.title