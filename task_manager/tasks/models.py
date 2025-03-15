from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """_summary_

    This model stores the details of a task, including its name, description, status, 
    and the user responsible for it.
    """
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    name = models.CharField(
        max_length=255,
    )
    
    description = models.TextField()
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES,
        default='pending',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
