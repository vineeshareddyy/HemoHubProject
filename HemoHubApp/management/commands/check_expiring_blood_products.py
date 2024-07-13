from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from HemoHubApp.models import PersonData, Notification

class Command(BaseCommand):
    help = 'Check and create notifications for expiring blood products'

    def handle(self, *args, **kwargs):
        self.check_expiring_blood_products()

    def check_expiring_blood_products(self):
        expiring_products = PersonData.objects.filter(Expiry_Date__lte=datetime.now() + timedelta(days=7))
        for product in expiring_products:
            message = f"The following blood product is expiring soon:\n\nPerson Name: {product.Person_Name}\nBlood Type: {product.Blood_Type}\nComponent: {product.Component}\nQuantity: {product.Quantity}\nExpiry Date: {product.Expiry_Date}\n\nPlease take the necessary actions."
            Notification.objects.create(
                message=message,
                is_read=False,
                person_data=product
            )
        self.stdout.write(self.style.SUCCESS('Successfully checked and updated notifications for expiring blood products'))
