# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Filmy(models.Model):
    filmid = models.AutoField(db_column='FilmID', primary_key=True)  # Field name made lowercase.
    tytul = models.CharField(db_column='Tytul', max_length=100, blank=True, null=True)  # Field name made lowercase.
    opis = models.TextField(db_column='Opis', blank=True, null=True)  # Field name made lowercase.
    gatunekid = models.ForeignKey('Gatunek', models.DO_NOTHING, db_column='GatunekID')  # Field name made lowercase.
    rezyserid = models.ForeignKey('Rezyser', models.DO_NOTHING, db_column='RezyserID')  # Field name made lowercase.
    czastrwania = models.SmallIntegerField(db_column='CzasTrwania', blank=True, null=True)  # Field name made lowercase.
    rokprodukcji = models.SmallIntegerField(db_column='RokProdukcji', blank=True, null=True)  # Field name made lowercase.
    wiekodbiorcy = models.IntegerField(db_column='WiekOdbiorcy', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.tytul + " (" + str(self.rokprodukcji) + ")"
    
    class Meta:
        managed = False
        db_table = 'filmy'


class Gatunek(models.Model):
    gatunekid = models.AutoField(db_column='GatunekID', primary_key=True)  # Field name made lowercase.
    nazwagatunku = models.CharField(db_column='NazwaGatunku', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gatunek'


class Jezyki(models.Model):
    jezykid = models.AutoField(db_column='JezykID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jezyki'


class Klienci(models.Model):
    klientid = models.AutoField(db_column='KlientID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'klienci'


class Pracownicy(models.Model):
    pracownikid = models.AutoField(db_column='PracownikID', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stanowiskoid = models.ForeignKey('Stanowisko', models.DO_NOTHING, db_column='StanowiskoID')  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=255, blank=True, null=True)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pracownicy'


class Rezerwacje(models.Model):
    rezerwacjaid = models.AutoField(db_column='RezerwacjaID', primary_key=True)  # Field name made lowercase.
    klientid = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='KlientID')  # Field name made lowercase.
    seansid = models.ForeignKey('Seanse', models.DO_NOTHING, db_column='SeansID')  # Field name made lowercase.
    miejsce = models.CharField(db_column='Miejsce', max_length=4, blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey('Statusrezerwacji', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
    datazlozenia = models.DateTimeField(db_column='DataZlozenia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rezerwacje'


class Rezyser(models.Model):
    rezyserid = models.AutoField(db_column='RezyserID', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rezyser'


class Salekinowe(models.Model):
    salaid = models.AutoField(db_column='SalaID', primary_key=True)  # Field name made lowercase.
    numer = models.IntegerField(db_column='Numer', blank=True, null=True)  # Field name made lowercase.
    liczbamiejsc = models.SmallIntegerField(db_column='LiczbaMiejsc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salekinowe'


class Seanse(models.Model):
    seansid = models.AutoField(db_column='SeansID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    godzina = models.TimeField(db_column='Godzina', blank=True, null=True)  # Field name made lowercase.
    salaid = models.ForeignKey(Salekinowe, models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.
    filmid = models.ForeignKey(Filmy, models.DO_NOTHING, db_column='FilmID')  # Field name made lowercase.
    dubbingid = models.ForeignKey(Jezyki, models.DO_NOTHING, db_column='DubbingID')  # Field name made lowercase.
    napisyid = models.ForeignKey(Jezyki, models.DO_NOTHING, db_column='NapisyID', related_name='seanse_napisyid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seanse'


class Stanowisko(models.Model):
    stanowiskoid = models.AutoField(db_column='StanowiskoID', primary_key=True)  # Field name made lowercase.
    nazwastanowiska = models.CharField(db_column='NazwaStanowiska', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stanowisko'


class Statusrezerwacji(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statusrezerwacji'

class FilmyKlient(models.Model):
    tytul = models.CharField(db_column='Tytul', max_length=100, blank=True, null=False, primary_key=True)  # Field name made lowercase.
    opis = models.TextField(db_column='Opis', blank=True, null=True)  # Field name made lowercase.
    nazwagatunku = models.CharField(db_column='NazwaGatunku', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=50, blank=True, null=True)  # 
    czastrwania = models.SmallIntegerField(db_column='CzasTrwania', blank=True, null=True)  # Field name made lowercase.
    rokprodukcji = models.SmallIntegerField(db_column='RokProdukcji', blank=True, null=True)  # Field name made lowercase.
    wiekodbiorcy = models.IntegerField(db_column='WiekOdbiorcy', blank=True, null=True)  # Field

    class Meta:
        managed = False
        db_table = 'filmyklient'

class RezerwacjaKlient(models.Model):
    seansid = models.IntegerField(db_column='SeansID', primary_key=True)  # Field name made lowercase.
    miejsce = models.CharField(db_column='Miejsce', max_length=4, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'rezerwacjaklient'


class SeansKlient(models.Model):
    data = models.DateField(db_column='Data', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    godzina = models.TimeField(db_column='Godzina', blank=True, null=True)  # Field name made lowercase.
    salaid = models.IntegerField(db_column='NumerSali')  # Field name 
    tytul = models.CharField(db_column='Tytul', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seansid = models.IntegerField(db_column='SeansID')  # Field name made lowercase.
    jezykDubbingu = models.CharField(db_column='JezykDubbingu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jezykNapisow = models.CharField(db_column='JezykNapisow', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seansklient'