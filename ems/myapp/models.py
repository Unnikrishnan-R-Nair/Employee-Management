from django.db import models

# Create your models here.


STATUS_CHOICE = {
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
}

GENDER_CHOICE = {
    ('Male', 'Male'),
    ('Female', 'Female'),
} 




class EmployeeDetails(models.Model):

    emp_id = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    email = models.CharField(max_length=200)

    address = models.CharField(max_length=300, blank=True, null=True)

    gender = models.CharField(max_length=50, choices=GENDER_CHOICE, default='Male')

    dob = models.DateField(blank=True,null=True)

    date_hired = models.DateField()

    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='Active')

    department = models.CharField(max_length=200)

    position = models.CharField(max_length=200)

    salary = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to="images", default="images/default.jpg", blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)

    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):

        return (self.first_name + ' ' + self.last_name)