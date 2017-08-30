from django.db import models
from datetime import datetime
class temp_read(models.Model):

    temp = models.IntegerField()
    dt = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.temp)
