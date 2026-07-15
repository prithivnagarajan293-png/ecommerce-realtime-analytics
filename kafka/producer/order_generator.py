from faker import Faker
import random

fake = Faker()

products = [
    "Laptop",
    "Mobile Phone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Smart Watch"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]


def generate_order():

    return {
        "order_id": random.randint(100000, 999999),
        "customer_id": random.randint(1000, 9999),
        "customer_name": fake.name(),
        "city": fake.city(),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(500, 80000), 2),
        "payment_method": random.choice(payment_methods),
        "order_timestamp": fake.iso8601()
    }