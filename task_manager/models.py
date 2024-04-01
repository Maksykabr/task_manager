from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    selected_data = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    completed = models.BooleanField(default=False)

    @property
    def day_of_week(self):
        return datetime.strftime(self.selected_date, '%A')

    def __str__(self):
        return self.title
