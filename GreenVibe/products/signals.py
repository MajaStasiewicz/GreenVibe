from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NewDelivery, ProductStorage, ProductEmpty

@receiver(post_save, sender=NewDelivery)
def update_storage_quantity(sender, instance, **kwargs):
    if kwargs['created']:
        option = instance.option 

        product_storages = ProductStorage.objects.filter(product__name=instance.product, option=option)

        for product_storage in product_storages:
            product_storage.storage += instance.quantity
            product_storage.save()

@receiver(post_save, sender=NewDelivery)
def update_product_empty(sender, instance, created, **kwargs):
    if created:
        try:
            product_empty = ProductEmpty.objects.get(product=instance.product)
            product_empty.delete()
        except ProductEmpty.DoesNotExist:
            pass 

@receiver(post_save, sender=ProductStorage)
def update_product_empty(sender, instance, **kwargs):
    if instance.storage <= 0:
        ProductEmpty.objects.get_or_create(product=instance.product)