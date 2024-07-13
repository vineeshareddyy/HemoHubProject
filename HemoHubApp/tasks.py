# your_app/tasks.py

from celery import shared_task
from .models import PersonData, Notification
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

@shared_task
def check_expiring_blood_products():
    try:
        logger.info("Task check_expiring_blood_products started")
        print("Task check_expiring_blood_products started")
        
        # Test database connectivity
        test_product_count = PersonData.objects.count()
        logger.info(f"Number of products in database: {test_product_count}")
        print(f"Number of products in database: {test_product_count}")
        
        expiring_products = PersonData.objects.filter(Expiry_Date__lte=datetime.now() + timedelta(days=7))
        if not expiring_products.exists():
            logger.info("No expiring products found")
            print("No expiring products found")
        
        for product in expiring_products:
            message = f"The following blood product is expiring soon:\n\nPerson Name: {product.Person_Name}\nBlood Type: {product.Blood_Type}\nComponent: {product.Component}\nQuantity: {product.Quantity}\nExpiry Date: {product.Expiry_Date}\n\nPlease take the necessary actions."
            Notification.objects.create(
                message=message,
                is_read=False,
                person_data=product
            )
            logger.info(f'Notification created for product {product.id}')
            print(f'Notification created for product {product.id}')
    except Exception as e:
        logger.error(f"Error in check_expiring_blood_products: {e}")
        print(f"Error in check_expiring_blood_products: {e}")
