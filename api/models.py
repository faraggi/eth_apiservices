from django.db import models


class Transaction(models.Model):
    tx_hash = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    from_addr = models.CharField(max_length=42)
    to_addr = models.CharField(max_length=42)
    value = models.FloatField()
    gasusedbytx = models.FloatField()
