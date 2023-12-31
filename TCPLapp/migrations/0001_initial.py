# Generated by Django 4.2.4 on 2023-10-07 12:11

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dhankawadi',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'dhankawadi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DhankawadiWards',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('wardnum', models.CharField(blank=True, max_length=50, null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'Dhankawadi_wards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DhankawdiRoad',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=320, null=True)),
                ('road_width', models.CharField(blank=True, db_column='Road_width', max_length=50, null=True)),
                ('missing_existing', models.CharField(blank=True, db_column='Missing_Existing', max_length=50, null=True)),
                ('length_m', models.FloatField(blank=True, db_column='Length_m', null=True)),
                ('wardnum', models.CharField(blank=True, max_length=50, null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
            ],
            options={
                'db_table': 'Dhankawdi_Road',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalPlu',
            fields=[
                ('fid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('taluka', models.CharField(blank=True, db_column='TALUKA', max_length=50, null=True)),
                ('broad_lu', models.CharField(blank=True, db_column='Broad_LU', max_length=50, null=True)),
                ('detailed_l', models.CharField(blank=True, db_column='Detailed_L', max_length=50, null=True)),
                ('descriptio', models.CharField(blank=True, db_column='Descriptio', max_length=150, null=True)),
                ('label', models.CharField(blank=True, db_column='Label', max_length=50, null=True)),
                ('area_ha', models.FloatField(blank=True, db_column='Area_HA', null=True)),
                ('plu_zone', models.CharField(blank=True, db_column='PLU_Zone', max_length=100, null=True)),
                ('reservatio', models.CharField(blank=True, db_column='Reservatio', max_length=50, null=True)),
                ('pa_name', models.CharField(blank=True, db_column='PA_Name', max_length=50, null=True)),
                ('growth_centre', models.CharField(blank=True, db_column='Growth_Centre', max_length=100, null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'Final_PLU',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmcMissingLinkBuffer',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('ward_name', models.CharField(blank=True, db_column='Ward_Name', max_length=80, null=True)),
                ('name_1', models.CharField(blank=True, db_column='Name_1', max_length=255, null=True)),
                ('road_width', models.CharField(blank=True, db_column='Road_width', max_length=255, null=True)),
                ('road_buffer', models.FloatField(blank=True, db_column='Road_Buffer', null=True)),
                ('buff_dist', models.FloatField(blank=True, db_column='BUFF_DIST', null=True)),
                ('orig_fid', models.IntegerField(blank=True, db_column='ORIG_FID', null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'PMC_Missing_Link_Buffer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmcMissingLinks',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('ward_name', models.CharField(blank=True, db_column='Ward_Name', max_length=80, null=True)),
                ('name_1', models.CharField(blank=True, db_column='Name_1', max_length=255, null=True)),
                ('road_width', models.CharField(blank=True, db_column='Road_width', max_length=255, null=True)),
                ('road_buffer', models.FloatField(blank=True, db_column='Road_Buffer', null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
            ],
            options={
                'db_table': 'PMC_Missing_Links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PuneAdminWards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('ward_name', models.CharField(blank=True, db_column='Ward_Name', max_length=200, null=True)),
            ],
            options={
                'db_table': 'pune-admin-wards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gutno', models.CharField(max_length=200)),
                ('villagename', models.CharField(max_length=200)),
                ('ownername', models.CharField(max_length=200)),
                ('Buildingtype', models.CharField(choices=[('Sanctioned', 'Sanctioned'), ('NotSanctioned', 'NotSanctioned')], max_length=200)),
                ('comment', models.CharField(default='comment', max_length=200)),
                ('upload_file', models.FileField(blank=True, upload_to='file/')),
            ],
            options={
                'db_table': 'TCPLapp_query',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Revenue1',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('gut_number', models.CharField(blank=True, db_column='Gut_Number', max_length=50, null=True)),
                ('taluka', models.CharField(blank=True, db_column='Taluka', max_length=50, null=True)),
                ('area_in_ha', models.FloatField(blank=True, db_column='Area_In_Ha', null=True)),
                ('source', models.CharField(blank=True, db_column='Source', max_length=200, null=True)),
                ('govtland_gayran_type', models.CharField(blank=True, db_column='GovtLand_Gayran_Type', max_length=50, null=True)),
                ('govt_private_forest_type', models.CharField(blank=True, db_column='Govt_Private_Forest_Type', max_length=50, null=True)),
                ('govtland_forest_7_12_availibility', models.CharField(blank=True, db_column='GovtLand_Forest_7_12_Availibility', max_length=50, null=True)),
                ('govtland_forest_as_7_12_full_part', models.CharField(blank=True, db_column='GovtLand_Forest_as_7_12_Full_Part', max_length=50, null=True)),
                ('old_gut_no', models.CharField(blank=True, db_column='Old_Gut_No', max_length=50, null=True)),
                ('new_gut_no', models.CharField(blank=True, db_column='New_Gut_No', max_length=50, null=True)),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=100, null=True)),
                ('village_name_census', models.CharField(blank=True, db_column='Village_Name_Census', max_length=255, null=True)),
                ('village_name_revenue', models.CharField(blank=True, db_column='Village_Name_Revenue', max_length=255, null=True)),
                ('temp', models.IntegerField(blank=True, db_column='Temp', null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
                ('village_taluka', models.CharField(blank=True, db_column='Village_Taluka', max_length=5000, null=True)),
            ],
            options={
                'db_table': 'revenue1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('objectid', models.BigIntegerField(db_column='OBJECTID', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=320, null=True)),
                ('road_width', models.CharField(blank=True, db_column='Road_width', max_length=50, null=True)),
                ('missing_existing', models.CharField(blank=True, db_column='Missing_Existing', max_length=50, null=True)),
                ('length_m', models.FloatField(blank=True, db_column='Length_m', null=True)),
                ('wardnum', models.CharField(blank=True, max_length=50, null=True)),
                ('shapelength', models.CharField(blank=True, db_column='shapeLength', max_length=50, null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
            ],
            options={
                'db_table': 'Road',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VillageBoundary',
            fields=[
                ('fid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('objectid', models.BigIntegerField(blank=True, db_column='OBJECTID', null=True)),
                ('taluka', models.CharField(blank=True, db_column='Taluka', max_length=50, null=True)),
                ('area_in_ha', models.FloatField(blank=True, db_column='Area_In_Ha', null=True)),
                ('village_name_census', models.CharField(blank=True, db_column='Village_Name_Census', max_length=255, null=True)),
                ('village_name_revenue', models.CharField(blank=True, db_column='Village_Name_Revenue', max_length=255, null=True)),
                ('temp', models.IntegerField(blank=True, db_column='Temp', null=True)),
                ('shape_length', models.FloatField(blank=True, db_column='Shape_Length', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'village_boundary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='villagetalukadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(max_length=200)),
                ('taluka', models.CharField(max_length=100)),
                ('gut', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files1', models.FileField(blank=True, upload_to='file/')),
                ('user_id1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField(default=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Name', max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DownloadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files1', models.FileField(blank=True, upload_to='file')),
                ('user_id1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=250)),
                ('city', models.TextField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('mobileno', models.BigIntegerField()),
                ('occupation', models.CharField(choices=[('others', 'others'), ('architect', 'architect'), ('builder', 'builder'), ('land owner', 'land owner'), ('liaison', 'liaison')], max_length=200)),
                ('industry', models.CharField(choices=[('civil', 'Civil'), ('govt', 'Government'), ('private', 'Private'), ('ngo', 'NGO'), ('other', 'Other')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
