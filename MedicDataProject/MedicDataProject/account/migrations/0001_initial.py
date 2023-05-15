# Generated by Django 4.1.7 on 2023-05-10 21:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrtname', models.CharField(max_length=255, verbose_name='Nombre del usuario')),
                ('lastname', models.CharField(max_length=255, verbose_name='Apellidos del paciente')),
                ('opinion', models.CharField(max_length=255, verbose_name='opinion')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre(s)')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('telefonoc', models.CharField(max_length=255, verbose_name='Teléfono celular')),
                ('telconsultorio', models.CharField(max_length=255, verbose_name='Telefono consultorio')),
                ('lugart', models.CharField(max_length=255, verbose_name='Lugar de trabajo')),
                ('direcciont', models.CharField(max_length=255, verbose_name='Direccion de trabajo')),
                ('especialidad', models.CharField(max_length=255, verbose_name='Especilidad general')),
                ('otras', models.CharField(max_length=255, verbose_name='Otras Especilidades')),
                ('profile_title', models.ImageField(blank=True, default='titulo.png', null=True, upload_to='')),
                ('profile_pic', models.ImageField(blank=True, default='perfil.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nombre del usuario')),
                ('apell', models.CharField(max_length=255, verbose_name='Apellidos del paciente')),
                ('edad', models.CharField(max_length=255, verbose_name='Edad del paciente')),
                ('telc', models.CharField(max_length=255, verbose_name='Teléfono celular')),
                ('domicilio', models.CharField(max_length=255, verbose_name='Domicilio')),
                ('seguro', models.CharField(max_length=255, verbose_name='Seguro Medico')),
                ('profile_pic', models.ImageField(blank=True, default='perfil1.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpedienteO',
            fields=[
                ('idEo', models.AutoField(primary_key=True, serialize=False)),
                ('nombreO', models.CharField(max_length=255, verbose_name='Nombre del paciente')),
                ('edadO', models.CharField(max_length=255, verbose_name='Edad del paciente')),
                ('gojoD', models.CharField(max_length=255, verbose_name='Graduacion ojo derecho')),
                ('gojoI', models.CharField(max_length=255, verbose_name='Graduacion ojo izquierdo')),
                ('padecimientos', models.CharField(max_length=255, verbose_name='Padecimientos')),
                ('cambioMicas', models.CharField(max_length=255, verbose_name='Cambio de micas')),
                ('fechaO', models.DateTimeField(auto_now_add=True)),
                ('fecha_actO', models.DateField(auto_now=True)),
                ('idDo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctoro', to=settings.AUTH_USER_MODEL, verbose_name='Usuario doctor')),
                ('idPg', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pacienteo', to=settings.AUTH_USER_MODEL, verbose_name='Usuario paciente')),
            ],
            options={
                'ordering': ('nombreO',),
            },
        ),
        migrations.CreateModel(
            name='ExpedienteG',
            fields=[
                ('idEg', models.AutoField(primary_key=True, serialize=False)),
                ('nombreG', models.CharField(max_length=255, verbose_name='Nombre del paciente')),
                ('edadG', models.CharField(max_length=255, verbose_name='Edad del paciente')),
                ('peso', models.CharField(max_length=20, verbose_name='Talla')),
                ('operaciones', models.CharField(max_length=255, verbose_name='Operaciones')),
                ('lesiones', models.CharField(max_length=255, verbose_name='Lesiones')),
                ('alergias', models.CharField(max_length=255, verbose_name='Alergias')),
                ('enfermedades', models.CharField(max_length=255, verbose_name='Enfermedades')),
                ('tipoSangre', models.CharField(max_length=255, verbose_name='Tipo de Sangre')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_actG', models.DateTimeField(auto_now=True)),
                ('idDg', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, verbose_name='Usuario doctor')),
                ('idPg', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL, verbose_name='Usuario paciente')),
            ],
            options={
                'ordering': ('nombreG',),
            },
        ),
        migrations.CreateModel(
            name='ExpedienteD',
            fields=[
                ('idEd', models.AutoField(primary_key=True, serialize=False)),
                ('nombreD', models.CharField(max_length=255, verbose_name='Nombre del paciente')),
                ('edadD', models.CharField(max_length=255, verbose_name='Edad del paciente')),
                ('NDiente1', models.CharField(max_length=255, verbose_name='Nombre del diente1')),
                ('NDiente2', models.CharField(max_length=255, verbose_name='Nombre del diente2')),
                ('NDiente3', models.CharField(max_length=255, verbose_name='Nombre del diente3')),
                ('NDiente4', models.CharField(max_length=255, verbose_name='Nombre del diente4')),
                ('NDiente5', models.CharField(max_length=255, verbose_name='Nombre del diente5')),
                ('Descripcion', models.CharField(max_length=550, verbose_name='Descripcion')),
                ('fechaD', models.DateTimeField(auto_now_add=True)),
                ('fecha_actD', models.DateField(auto_now=True)),
                ('idDd', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctord', to=settings.AUTH_USER_MODEL, verbose_name='Usuario doctor')),
                ('idPg', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciented', to=settings.AUTH_USER_MODEL, verbose_name='Usuario paciente')),
            ],
            options={
                'ordering': ('nombreD',),
            },
        ),
    ]
