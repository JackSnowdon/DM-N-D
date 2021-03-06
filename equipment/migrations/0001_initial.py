# Generated by Django 2.0.2 on 2019-12-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Die',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('die', models.CharField(choices=[('D4', '4'), ('D6', '6'), ('D8', '8'), ('D10', '10'), ('D12', '12'), ('D20', '20')], default='D4', max_length=20)),
                ('number_of_die', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('die', models.ManyToManyField(to='equipment.Die')),
            ],
        ),
    ]
