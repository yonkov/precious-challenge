# Generated by Django 2.2.5 on 2019-12-04 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20191126_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='cost',
            field=models.IntegerField(help_text='Cost of the service'),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='trip',
            field=models.ForeignKey(blank=True, help_text='Add the service to its corresponding trip', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accomodations', to='trips.Trip'),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='typeOfService',
            field=models.CharField(default='accomodation', help_text='The name of the service, e.g. hotel, accomodation or transportation', max_length=64),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='cost',
            field=models.IntegerField(help_text='Cost of the service'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='trip',
            field=models.ForeignKey(blank=True, help_text='Add the service to its corresponding trip', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='trips.Trip'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='typeOfService',
            field=models.CharField(default='hotel', help_text='The name of the service, e.g. hotel, accomodation or transportation', max_length=64),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='cost',
            field=models.IntegerField(help_text='Cost of the service'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='trip',
            field=models.ForeignKey(blank=True, help_text='Add the service to its corresponding trip', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transportations', to='trips.Trip'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='typeOfService',
            field=models.CharField(default='transportation', help_text='The name of the service, e.g. hotel, accomodation or transportation', max_length=64),
        ),
    ]
