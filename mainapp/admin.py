from django.contrib import admin

from .models import BaseModel, SponsorModel, StudentModel, StudentSponsor, UniversityModel

# Register your models here.

admin.register(BaseModel)

@admin.register(SponsorModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'amount', 'organization', 'phone')
    list_display_links = ('id', 'sponsor', 'amount')
    search_fields = ('sponsor', 'organization')
    list_filter = ('amount',)
    
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name',)
admin.register(StudentSponsor)
admin.register(UniversityModel)