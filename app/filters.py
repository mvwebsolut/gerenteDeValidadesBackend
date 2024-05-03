import string
from datetime import datetime

def sort_products_by_expiration(products):
    return sorted(products, key=lambda x: x.validity_date)
def get_badger_color(date):

    if int(date) <= 7:
        return "bg-red-500"
    elif int(date) <= 30:
        return "bg-yellow-500"
    else:
        return "bg-green-500"

def get_badger_category_color(products):
    today = datetime.today()
    products = sort_products_by_expiration(products)
    for product in products:
        days_remaining = (product.validity_date - today).days
        if days_remaining <= 7:
            return 'bg-red-500'
        elif days_remaining <= 30:
            return 'bg-yellow-500'
    return "bg-green-500"

def category_name_formater(category):
    if category == "" or category is None:
        return "Sem categoria"
    return category
