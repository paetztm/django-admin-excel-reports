from django.db import models


class Artist(models.Model):
    artist_id = models.IntegerField(db_column='ArtistId', primary_key=True)
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'Artist'

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.IntegerField(db_column='AlbumId', primary_key=True)
    title = models.CharField(db_column='Title', blank=True, null=True, max_length=160)
    artist = models.ForeignKey(Artist, db_column='ArtistId')

    class Meta:
        managed = False
        db_table = 'Album'

    def __str__(self):
        return self.title


class Employee(models.Model):
    employee_id = models.IntegerField(db_column='EmployeeId', primary_key=True)
    first_name = models.CharField(db_column='FirstName', blank=True, null=True, max_length=20)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=20)
    title = models.CharField(db_column='Title', blank=True, null=True, max_length=30)
    reports_to = models.ForeignKey("self", db_column='ReportsTo', blank=True, null=True)
    birth_date = models.DateField(db_column='BirthDate', blank=True, null=True)
    hire_date = models.DateField(db_column='HireDate', blank=True, null=True)
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=70)
    city = models.CharField(db_column='City', blank=True, null=True, max_length=40)
    state = models.CharField(db_column='State', blank=True, null=True, max_length=40)
    country = models.CharField(db_column='Country', blank=True, null=True, max_length=40)
    postal_code = models.CharField(db_column='PostalCode', blank=True, null=True, max_length=10)
    phone = models.CharField(db_column='Phone', blank=True, null=True, max_length=24)
    fax = models.CharField(db_column='Fax', blank=True, null=True, max_length=24)
    email = models.EmailField(db_column='Email', blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'Employee'

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Customer(models.Model):
    customer_id = models.IntegerField(db_column='CustomerId', primary_key=True)
    first_name = models.CharField(db_column='FirstName', blank=True, null=True, max_length=40)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=20)
    company = models.CharField(db_column='Company', blank=True, null=True, max_length=80)
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=70)
    city = models.CharField(db_column='City', blank=True, null=True, max_length=40)
    state = models.CharField(db_column='State', blank=True, null=True, max_length=40)
    country = models.CharField(db_column='Country', blank=True, null=True, max_length=40)
    postal_code = models.CharField(db_column='PostalCode', blank=True, null=True, max_length=10)
    phone = models.CharField(db_column='Phone', blank=True, null=True, max_length=24)
    fax = models.CharField(db_column='Fax', blank=True, null=True, max_length=24)
    email = models.EmailField(db_column='Email', blank=True, null=True, max_length=60)
    support_rep = models.ForeignKey(Employee, db_column='SupportRepId')

    class Meta:
        managed = False
        db_table = 'Customer'

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Genre(models.Model):
    genre_id = models.IntegerField(db_column='GenreId', primary_key=True)
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'Genre'

    def __str__(self):
        return self.name


class MediaType(models.Model):
    media_type_id = models.IntegerField(db_column='MediaTypeId', primary_key=True)
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'MediaType'

    def __str__(self):
        return self.name


class Playlist(models.Model):
    playlist_id = models.IntegerField(db_column='PlaylistId', primary_key=True)
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'Playlist'

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_id = models.IntegerField(db_column='InvoiceId', primary_key=True)
    customer = models.ForeignKey(Customer, db_column='CustomerId')
    invoice_date = models.DateTimeField(db_column='InvoiceDate')
    billing_address = models.CharField(db_column='BillingAddress', blank=True, null=True, max_length=70)
    billing_city = models.CharField(db_column='BillingCity', blank=True, null=True, max_length=40)
    billing_state = models.CharField(db_column='BillingState', blank=True, null=True, max_length=40)
    billing_country = models.CharField(db_column='BillingCountry', blank=True, null=True, max_length=40)
    billing_postal_code = models.CharField(db_column='BillingPostalCode', blank=True, null=True, max_length=10)
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Invoice'

    def __str__(self):
        return str(self.invoice_id)


class Track(models.Model):
    track_id = models.IntegerField(db_column='TrackId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=200)
    album = models.ForeignKey(Album, db_column='AlbumId', blank=True, null=True)
    media_type = models.ForeignKey(MediaType, db_column='MediaTypeId')
    genre = models.ForeignKey(Genre, db_column='GenreId', blank=True, null=True)
    composer = models.CharField(db_column='Composer', blank=True, null=True, max_length=220)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unit_price = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Track'

    def __str__(self):
        return self.name


class InvoiceLine(models.Model):
    invoice_line_id = models.IntegerField(db_column='InvoiceLineId', primary_key=True)
    invoice = models.ForeignKey(Invoice, db_column='InvoiceId')
    track = models.ForeignKey(Track, db_column='TrackId')
    unit_price = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(db_column='Quantity')

    class Meta:
        managed = False
        db_table = 'InvoiceLine'

    def __str__(self):
        return str(self.invoice_line_id)


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, db_column='PlaylistId')
    track = models.ForeignKey(Track, db_column='TrackId')

    class Meta:
        managed = False
        db_table = 'PlaylistTrack'
        unique_together = (('playlist', 'track'),)

