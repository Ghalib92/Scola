# Generated by Django 5.1.6 on 2025-03-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_meal', '0008_weightmanagementfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightmanagementfood',
            name='category',
            field=models.CharField(choices=[('weight_increase', 'Weight_Increase'), ('weight_loss', 'Weight_Loss'), ('weight_retantion', 'Weight_Retantion')], max_length=20),
        ),
    ]
