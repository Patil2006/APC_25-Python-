from products.product_details import product_details
from products.product_search import search_product
from customers.customer_details import customer_details
from customers.customer_registration import register_customer
from orders.create_order import create_order
from orders.order_status import order_status
from payments.payment import make_payment
from payments.refund import refund

product_details()
search_product("Laptop")

customer_details()
register_customer("Bhakti")

create_order("Laptop")
order_status()

make_payment(50000)
refund(5000)