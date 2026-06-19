from django.db import models

class Ticket(models.Model):

    CATEGORY_CHOICES = [
        ('Billing', 'Billing'),
        ('Technical', 'Technical'),
        ('Refund', 'Refund'),
        ('Account', 'Account'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=100,
        blank=True
    )

    priority = models.CharField(
        max_length=20,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
# Create your models here.
