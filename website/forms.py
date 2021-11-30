from django import forms
from .models import Inwarding

# This class is for inserting inwards in the Inwarding model.  The fields array are the only ones you wish to save during insert 
class InwardingForm(forms.ModelForm):
    class Meta:
        model = Inwarding
        fields = ['inw_item_name', 'inw_location', 'inw_description', 'inw_make_model', 'inw_quantity', 'inw_vendor_name', 'inw_date_of_purchase', 'inw_unit_cost', 'inw_category', 'inw_type', 'inw_remarks', 'inw_owner', 'inw_sourcing_department', 'inw_user_group', 'inw_img']

# This class is for updating inwards in the Inwarding model.  The fields array are the only ones you wish to save during update
class InwardingFormEdit(forms.ModelForm):
    class Meta:
        model = Inwarding
        fields = ['inw_item_name', 'inw_location', 'inw_description', 'inw_make_model', 'inw_quantity', 'inw_vendor_name', 'inw_date_of_purchase', 'inw_unit_cost', 'inw_category', 'inw_type', 'inw_remarks', 'inw_img']

# This class is for updating inwards in the Inwarding model.  The fields array are the only ones you wish to save during update
class InwardingFormHOD(forms.ModelForm):
    class Meta:
        model = Inwarding
        fields = ['inw_admin_approve']

# This class is for updating inwards in the Inwarding model.  The fields array are the only ones you wish to save during update
class InwardingFormFIN(forms.ModelForm):
    class Meta:
        model = Inwarding
        fields = ['inw_finance_approve']