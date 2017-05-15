from django.contrib import admin

from chinook.models import Track, Artist, Album, Employee, Customer, Invoice, InvoiceLine, Playlist, PlaylistTrack, \
    Genre, MediaType


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
    readonly_fields = ('album_id', )


class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('artist_id',)


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('customer_id',)
    list_display = ('__str__', 'address', 'city', 'state', 'country', 'postal_code')


class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('employee_id',)
    list_display = ('__str__', 'employee_id', 'address', 'city', 'state', 'country', 'postal_code')


class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('genre_id',)


class InvoiceLineAdmin(admin.ModelAdmin):
    readonly_fields = ('invoice_line_id',)
    list_display = ('__str__', 'invoice', 'track', 'unit_price', 'quantity')


class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ('invoice_id',)
    list_display = ('__str__', 'customer', 'invoice_date', 'total')


class MediaTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('media_type_id', )


class PlaylistAdmin(admin.ModelAdmin):
    readonly_fields = ('playlist_id',)


class TrackAdmin(admin.ModelAdmin):
    readonly_fields = ('track_id',)
    list_display = ('__str__', 'album', 'media_type', 'genre', 'composer', 'unit_price')

admin.site.register(Track, TrackAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceLine, InvoiceLineAdmin)
admin.site.register(Playlist, PlaylistAdmin)
# admin.site.register(PlaylistTrack)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MediaType, MediaTypeAdmin)


