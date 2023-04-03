# Generated by Django 4.1.5 on 2023-02-26 09:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocoUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("UNSPECIFIED", "Unspecified"),
                            ("DISTRIBUTOR", "Distributor"),
                            ("RETAILER", "Retailer"),
                            ("EMPLOYEE", "Employee"),
                            ("BUSINESS_ADMIN", "Business Admin"),
                            ("DOCO_ADMIN", "Doco Admin"),
                        ],
                        default="UNSPECIFIED",
                        max_length=20,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("address_line1", models.TextField()),
                ("address_line2", models.TextField()),
                ("is_verified", models.BooleanField(default=False)),
                ("latitude", models.TextField(blank=True, null=True)),
                ("longitude", models.TextField(blank=True, null=True)),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="common.area"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BusinessProfile",
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
                ("profile_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("UNKNOWN", "Unknown"),
                            ("DISTRIBUTOR", "Distributor"),
                            ("RETAILER", "Retailer"),
                        ],
                        default="UNKNOWN",
                        max_length=20,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("contact_person_name", models.CharField(max_length=50)),
                ("contact_person_designation", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("number_verified", models.BooleanField(default=False)),
                ("email_verified", models.BooleanField(default=False)),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="profile.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Document",
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
                ("file", models.FileField(upload_to="DOCUMENTS")),
                ("identification_number", models.TextField(blank=True, null=True)),
                ("expiry_date", models.DateField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="common.documenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RetailerProfile",
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
                (
                    "admin_user",
                    models.OneToOneField(
                        limit_choices_to={"type": "BUSINESS_ADMIN"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "business_profile",
                    models.OneToOneField(
                        limit_choices_to={"type": "RETAILER"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.businessprofile",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="EmployeeProfile",
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
                (
                    "employee_code",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("joining_date", models.DateField(null=True)),
                ("primary_number", models.CharField(max_length=15)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("number_verified", models.BooleanField(default=False)),
                ("email_verified", models.BooleanField(default=False)),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="profile.address",
                    ),
                ),
                (
                    "address_proof",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="employee_address_proof",
                        to="profile.document",
                    ),
                ),
                (
                    "employer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.businessprofile",
                    ),
                ),
                (
                    "id_proof",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="employee_id_proof",
                        to="profile.document",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        limit_choices_to={"type": "EMPLOYEE"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DistributorProfile",
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
                (
                    "tenant_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("code", models.CharField(max_length=4)),
                (
                    "admin_user",
                    models.OneToOneField(
                        limit_choices_to={"type": "BUSINESS_ADMIN"},
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="admin_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "api_user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        limit_choices_to={"type": "DISTRIBUTOR"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="api_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "business_profile",
                    models.OneToOneField(
                        limit_choices_to={"type": "DISTRIBUTOR"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.businessprofile",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="BusinessAdmin",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("profile.docouser",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Distributor",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("profile.docouser",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="DocoAdmin",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("profile.docouser",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("profile.docouser",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Retailer",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("profile.docouser",),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.AddIndex(
            model_name="employeeprofile",
            index=models.Index(
                fields=["employee_code", "primary_number", "employer"],
                name="profile_emp_employe_5a8de1_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="document",
            index=models.Index(
                fields=["identification_number"], name="profile_doc_identif_8ac247_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="businessprofile",
            index=models.Index(
                fields=["name", "contact_person_name", "type", "profile_id"],
                name="profile_bus_name_8a4f2f_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(fields=["area"], name="profile_add_area_id_a3723a_idx"),
        ),
    ]