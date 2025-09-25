import secrets
import string
from .models import Coupon

def generate_coupon_code(length=10):
    characters = string.ascii_letters + string.digits
    while True:
        coupon_code = ''.join(secrets.choice(characters) for _ in) range(length))
        if not Coupon.objects.filter(code=coupon_code).exists():
            return coupon_code