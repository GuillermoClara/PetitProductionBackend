# Generated by Django 4.1.1 on 2022-10-23 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.business')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=16)),
                ('works_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.business')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.CharField(default=None, max_length=50)),
                ('client_phone', models.CharField(default=None, max_length=16)),
                ('date', models.CharField(default=None, max_length=15)),
                ('start', models.CharField(default=None, max_length=5)),
                ('end', models.CharField(default=None, max_length=5)),
                ('service', models.CharField(default=None, max_length=100)),
                ('token', models.CharField(default=None, max_length=22)),
                ('address_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.address')),
                ('business_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.business')),
                ('provider_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='business_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.business'),
        ),
    ]
