from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# This is the class for inwarding, or equivalent to a table named Inwarding in your database
class Inwarding(models.Model):
    inw_item_name = models.CharField(max_length=200)
    inw_location = models.CharField(max_length=100)
    inw_description = models.CharField(max_length=200)
    inw_make_model = models.CharField(max_length=200)
    inw_quantity = models.IntegerField()
    inw_vendor_name = models.CharField(max_length=200)
    inw_date_of_purchase = models.DateField(max_length=200)
    inw_unit_cost = models.IntegerField()
    inw_category = models.CharField(max_length=200)
    inw_type = models.CharField(max_length=200)
    inw_remarks = models.TextField(blank=True)
    inw_admin_approve = models.BooleanField(default=False)
    inw_finance_approve = models.BooleanField(default=False)
    inw_date_of_entry= models.DateField(default=now)
    inw_owner = models.CharField(max_length=200)
    inw_sourcing_department = models.CharField(max_length=200)
    inw_user_group = models.CharField(max_length=200)
    inw_img = models.ImageField(null=True, blank=True, upload_to="receipts/")

    # This is the output in your admin area, it will return only the item name
    def __str__(self):
        return self.inw_item_name

# This is the dropdown choices for filter group
GROUP_CHOICES = (
    ('HOD','HOD'),
    ('FINANCE','FINANCE'),
    ('EMPLOYEE','EMPLOYEE'),
    ('ADMIN','ADMIN'),
)

# This is the dropdown choices for department
DEPARMENT_CHOICES = (
    ('MANAGEMENT','MANAGEMENT'),
    ('OPERATIONS','OPERATIONS'),
    ('T&S','T&S'),
    ('NAVAC','NAVAC'),
    ('E&M','E&M'),
    ('S&S','S&S'),
    ('FCN','FCN'),
)

# This is the class for Filtering, or equivalent to a table named Filtering in your database
class Filtering(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_department = models.CharField(max_length=200, choices=DEPARMENT_CHOICES, default='MANAGEMENT')
    user_filter_group = models.CharField(max_length=200, choices=GROUP_CHOICES, default='HOD')

    # This is the output in your admin area, it will return the first name + department + group
    def __str__(self):
        return str(self.user.first_name) + ' | ' + str(self.user_department) + ' | ' + str(self.user_filter_group)