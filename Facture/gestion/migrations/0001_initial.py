# Generated by Django 4.2.8 on 2024-01-09 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('creat_date', models.DateTimeField(auto_now_add=True)),
                ('save_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date_time', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('last_update_date', models.DateTimeField(blank=True, null=True)),
                ('paie', models.BooleanField(default=False)),
                ('invoice_type', models.CharField(choices=[('R', 'Reçu'), ('P', 'PROFORMA'), ('F', 'FACTURE')], max_length=1)),
                ('comments', models.TextField(blank=True, max_length=1000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.customer')),
                ('save_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1000)),
                ('quantite', models.IntegerField()),
                ('prix_unit', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.invoice')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
