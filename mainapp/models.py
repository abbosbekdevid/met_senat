from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        abstract = True
    

class UniversityModel(BaseModel):
    title = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title
    
    
class SponsorModel(BaseModel):
    sponsor = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    organization = models.CharField(max_length=100)
    sponsor_type = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    payment_type = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.sponsor
    
    
class StudentModel(BaseModel):
    full_name = models.CharField(max_length=100)
    student_type = models.CharField(max_length=40)
    university_fk = models.ForeignKey(UniversityModel, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    contract = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.full_name
    
    
class StudentSponsor(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor_fk = models.ForeignKey(SponsorModel, on_delete=models.SET_NULL, null=True)
    student_fk = models.ForeignKey(StudentModel, on_delete=models.SET_NULL, null=True)
    
    
    