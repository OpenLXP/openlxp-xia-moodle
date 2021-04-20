# Generated by Django 3.1.7 on 2021-03-31 19:55

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetadataLedger',
            fields=[
                ('metadata_record_inactivation_date', models.DateTimeField(blank=True, null=True)),
                ('metadata_record_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('record_lifecycle_status', models.CharField(blank=True, choices=[('Active', 'A'), ('Inactive', 'I')], max_length=10)),
                ('source_metadata', models.JSONField(blank=True)),
                ('source_metadata_extraction_date', models.DateTimeField(auto_now_add=True)),
                ('source_metadata_hash', models.CharField(max_length=200)),
                ('source_metadata_key', models.TextField()),
                ('source_metadata_key_hash', models.CharField(max_length=200)),
                ('source_metadata_transformation_date', models.DateTimeField(blank=True, null=True)),
                ('source_metadata_validation_date', models.DateTimeField(blank=True, null=True)),
                ('source_metadata_validation_status', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('target_metadata', models.JSONField(default=dict)),
                ('target_metadata_hash', models.CharField(max_length=200)),
                ('target_metadata_key', models.TextField()),
                ('target_metadata_key_hash', models.CharField(max_length=200)),
                ('target_metadata_transmission_date', models.DateTimeField(blank=True, null=True)),
                ('target_metadata_transmission_status', models.CharField(blank=True, choices=[('Successful', 'S'), ('Failed', 'F'), ('Pending', 'P'), ('Ready', 'R')], default='Ready', max_length=10)),
                ('target_metadata_transmission_status_code', models.IntegerField(blank=True, null=True)),
                ('target_metadata_validation_date', models.DateTimeField(blank=True, null=True)),
                ('target_metadata_validation_status', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='XIAConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(default='DAU', help_text='Enter the source file to extract data from.', max_length=200)),
                ('source_metadata_schema', models.CharField(default='DAU_source_validate_schema.json', help_text='Enter the dau schema file', max_length=200)),
                ('source_target_mapping', models.CharField(default='DAU_p2881_target_metadata_schema.json', help_text='Enter the schema file to map target.', max_length=200)),
                ('target_metadata_schema', models.CharField(default='p2881_target_validation_schema.json', help_text='Enter the target schema file to validate from.', max_length=200)),
            ],
        ),
    ]
