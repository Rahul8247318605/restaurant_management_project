import secrets
import string
from .models import Coupon

def generate_coupon_code(length=10):
    characters = string.ascii_letters + string.digits
    while True:
        coupon_code = ''.join(secrets.choice(characters) for _ in) range(length))
        if not Coupon.objects.filter(code=coupon_code).exists():
            return coupon_code
def get_daily_sales_total(specific_date:date):
    orders=Order.objects.filter(created_at_date=specific_date)
    total_sales=orders.aggregate(total_sum=Sum('total_price'))['total_sum']
    return total_sales or 0