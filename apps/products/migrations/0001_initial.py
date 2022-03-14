# Generated by Django 4.0.2 on 2022-03-01 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='categories.category')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255, verbose_name='상품명')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='상품금액')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='상품설명')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제일')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-id'],
            },
        ),
    ]