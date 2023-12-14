from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import Survey
from custom.models import Municipality,AdministrativePost,Village

class DateInput(forms.DateInput):
	input_type = 'date'

class SurveyForm1(forms.ModelForm):
	surveyDate = forms.DateField(label='Data Survey', widget=DateInput())
	class Meta:
		model = Survey
		fields = ['programa','village','aldeia','surveyDate','image','description','totalUmakain']
		exclude = ['user_created','hashed','date_created','rejected_info','is_rejected','municipality','administrativepost']

	def __init__(self, *args, **kwargs):
		administrativepost = kwargs.pop('administrativepost',None)
		super().__init__(*args, **kwargs)
		self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost.id)
		self.fields['description'].widget.attrs['rows'] = 2

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('village', css_class='form-group col-md-6 mb-0'),
				Column('aldeia', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('programa', css_class='form-group col-md-4 mb-0'),
				Column('surveyDate', css_class='form-group col-md-4 mb-0'),
				Column('totalUmakain', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('description', css_class='form-group col-md-7 mb-0'),
				Column('image', css_class='form-group col-md-5 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class SurveyForm2(forms.ModelForm):
	surveyDate = forms.DateField(label='Data Survey', widget=DateInput())
	class Meta:
		model = Survey
		fields = ['programa','aldeia','totalUmakain','surveyDate','image','description']
		exclude = ['user_created','hashed','date_created','rejected_info','is_rejected','is_implemented','municipality','administrativepost','village']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['description'].widget.attrs['rows'] = 2
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('aldeia', css_class='form-group col-md-6 mb-0'),
				Column('totalUmakain', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('programa', css_class='form-group col-md-6 mb-0'),
				Column('surveyDate', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('description', css_class='form-group col-md-5 mb-0'),
				Column('image', css_class='form-group col-md-3 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)