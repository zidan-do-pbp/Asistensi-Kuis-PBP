from django.db import models


class Report(models.Model):
    STATUS_CHOICES = [
        ("hilang", "Hilang"),
        ("ditemukan", "Ditemukan"),
    ]

    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )