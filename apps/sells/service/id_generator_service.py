from apps.profile.models import DistributorProfile
from datetime import datetime


def generate_order_id(tenant_id):
    distributor = DistributorProfile.objects.get_distributor_for_tenant_id(tenant_id)
    if distributor is not None:
        now = datetime.now()
        time_string = now.strftime("%Y%m%d-%H%M%S")
        # TODO : This logic can break if there is more than one request at the exact moment for a distributor
        return f'ORD-{distributor.code}-{time_string}'


def generate_invoice_id(order):
    return f'INV-{order.order_id[4:]}'
