from django import forms
from .models import Resume

# gender n job_title is choices means it is checkbox so we have to work on it
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

JOB_CITY_CHOICE = (
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Ranchi', 'Ranchi'),
    ('Mumbai', 'Mumbai'),
    ('Assam', 'Assam'),
    ('Chennai', 'Chennai'),
    ('Dehradun', 'Dehradun'),
)


class ResumeForm(forms.ModelForm):
    # by default iska widget choice bala hota han so hume usse radio button karna padega widget set karke
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin',
                  'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        # beacuse in models u cant write Full Name means u cant write any name with space we have to write like this name or full_name
        labels = {'name': 'Full Name',
                  'dob': 'Date of Birth', 'pin': 'Pin Code', 'mobile': 'Mobile No.', 'email': 'Email Id', 'profile_image': 'Profile Image', 'my_file': 'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
