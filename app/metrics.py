from product.models import Product
from django.db.models import Sum, F
from outflow.models import Outflow
from django.utils import timezone


def get_product_metrics():
    products = Product.objects.all()

    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price
    items_in_stock = sum(product.quantity for product in products)
    low_stock = Product.objects.filter(quantity__lt=5)
    top_selling = Product.objects.order_by('-selling_price')[:5]
    latest_products = Product.objects.order_by('-created_at')[:5]

    return {
        "total_cost_price": total_cost_price,
        "total_selling_price": total_selling_price,
        "total_profit": total_profit,
        "items_in_stock": items_in_stock,
        "low_stock": low_stock,
        "top_selling": top_selling,
        "latest_products": latest_products,
    }


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(total_products_sold=Sum('quantity'))['total_products_sold'] or 0
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost
    return {
        "total_sales": total_sales,
        "total_products_sold": total_products_sold,
        "total_sales_value": total_sales_value,
        "total_sales_profit": total_sales_profit,
        "total_sales_cost": total_sales_cost,
    }


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales = Outflow.objects.filter(created_at__date=date).aggregate(total_sales=Sum(F('product__selling_price') * F('quantity')))['total_sales'] or 0
        values.append(float(sales))
    return {
        "dates": dates,
        "values": values
    }


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        values.append(sales_quantity)

    return {
        "dates": dates,
        "values": values
    }
