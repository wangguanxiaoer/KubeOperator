# Generated by Django 2.1.15 on 2020-02-16 08:14

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ko_host', '0001_initial'),
        ('ko_package', '0001_initial'),
        ('ansible_api', '0002_auto_20190305_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Project')),
                ('configs', common.models.JsonDictTextField(default={})),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ko_package.Package')),
            ],
            bases=('ansible_api.project',),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('host_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Host')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ko_host.Host')),
            ],
            options={
                'abstract': False,
            },
            bases=('ansible_api.host',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ansible_api.group',),
        ),
    ]
