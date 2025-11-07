from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WaterIntakeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity =  models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(default=timezone.now)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date') 

    def __str__(self):
        return f"{self.user.username} - {self.quantity}ml on {self.date}"
