# Generated by Django 4.1.5 on 2023-02-26 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profile", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(null=True, verbose_name="Deleted at"),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "order_id",
                    models.CharField(editable=False, max_length=40, unique=True),
                ),
                ("is_approved", models.BooleanField(default=False)),
                (
                    "approved_at",
                    models.DateTimeField(auto_now=True, verbose_name="Approved at"),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CART", "CART"),
                            ("CREATED", "CREATED"),
                            ("REJECTED", "CANCELLED"),
                            ("REJECTED", "REJECTED"),
                            ("APPROVED", "APPROVED"),
                            ("PREPARED", "PREPARED"),
                            ("OFD", "OFD"),
                            ("COMPLETED", "COMPLETED"),
                        ],
                        default="CREATED",
                        max_length=20,
                    ),
                ),
                ("order_value", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "approved_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="profile.employeeprofile",
                    ),
                ),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="profile.retailerprofile",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.distributorprofile",
                        to_field="tenant_id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(null=True, verbose_name="Deleted at"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sells.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stock.product"
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.distributorprofile",
                        to_field="tenant_id",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="stock.productunit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Modified at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(null=True, verbose_name="Deleted at"),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "invoice_id",
                    models.CharField(editable=False, max_length=40, unique=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("GENERATED", "GENERATED"),
                            ("PENDING", "PENDING"),
                            ("SETTLED", "SETTLED"),
                        ],
                        default="GENERATED",
                        max_length=20,
                    ),
                ),
                ("due_date", models.DateField()),
                ("invoice_value", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="sells.order"
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.distributorprofile",
                        to_field="tenant_id",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="orderitem",
            index=models.Index(
                fields=["order", "product"], name="sells_order_order_i_00de83_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="orderitem", unique_together={("order", "product")},
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["created_by", "order_id", "buyer", "tenant"],
                name="sells_order_created_f4bc20_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="invoice",
            index=models.Index(
                fields=["order", "invoice_id"], name="sells_invoi_order_i_e1f99d_idx"
            ),
        ),
    ]
