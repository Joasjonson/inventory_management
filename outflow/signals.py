from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
import requests
from services.notify import Notify
from datetime import datetime

@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
   if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, **kwargs):
    notify = Notify()

    data = {
        "action": "outflow_created",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id": instance.id,
        "product": instance.product.title,
        "quantity": instance.quantity,
    }
    notify.send_event(data)