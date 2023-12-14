from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from custom.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class MonitoringForm(forms.ModelForm):
	monitoring_date = forms.DateField(label='Data Monitoring', widget=DateInput())
	class Meta:
		model = ImplementationMonitoring
		fields = ['pursentu_programa','orsamentu_gastu','ekipamentu_lakompletu',\
				'komentariu','monitoring_date','faze','siklu','image']
		exclude = ['user_created','hashed','date_created','funsionariu','implementasaun','pursentu_acumulativa','orsamentu_acumulativa']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['komentariu'].widget.attrs['rows'] = 2
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('monitoring_date', css_class='form-group col-md-4 mb-0'),
				Column('pursentu_programa', css_class='form-group col-md-4 mb-0'),
				Column('orsamentu_gastu', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('ekipamentu_lakompletu', css_class='form-group col-md-6 mb-0'),
				Column('komentariu', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('faze', css_class='form-group col-md-4 mb-0'),
				Column('siklu', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class PostImplementationMonitoringForm(forms.ModelForm):
	monitoring_date = forms.DateField(label='Data Monitoring', widget=DateInput())
	class Meta:
		model = PostImplementationMonitoring
		fields = ['kondisaun','rekomendasaun','komentariu','monitoring_date','image']
		exclude = ['user_created','hashed','date_created','funsionariu','implementasaun']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['komentariu'].widget.attrs['rows'] = 2
		self.fields['rekomendasaun'].widget.attrs['rows'] = 2
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('monitoring_date', css_class='form-group col-md-6 mb-0'),
				Column('kondisaun', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('komentariu', css_class='form-group col-md-6 mb-0'),
				Column('rekomendasaun', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)