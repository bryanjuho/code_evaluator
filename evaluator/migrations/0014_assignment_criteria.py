# Generated by Django 4.0.4 on 2022-05-28 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0013_remove_criterion_assignment_remove_criterion_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='criteria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='evaluator.criterion', verbose_name='Criteria'),
        ),
    ]
