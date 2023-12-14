from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from survey.models import Survey
from custom.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class ProgramaForm(forms.ModelForm):
	class Meta:
		model = Programa
		fields = ['naran']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('naran', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class ImplementasaunForm(forms.ModelForm):
	startdate = forms.DateField(label='Data Hahu Implementasaun', widget=DateInput())
	enddate = forms.DateField(label='Data Remata Implementasaun', widget=DateInput())
	class Meta:
		model = Implementasaun
		fields = ['enddate','programa','municipality','administrativepost','village','montanteOsanAlokasaun','startdate','image','description','survey','partisipasaunF','totalTekniku','partisipasaunM','partisipasaunP']
		exclude = ['user_created','hashed','date_created','statusImplementasaun','rejected_info','is_rejected']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		implementedSurvey = Implementasaun.objects.all().values_list('survey__id',flat=True)
		usedSurveyID = Survey.objects.filter(id__in=implementedSurvey).values_list('id', flat=True)
		self.fields['survey'].queryset = Survey.objects.exclude(id__in=usedSurveyID).filter(is_approved=True)
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
				Column('survey', css_class='form-group col-md-3 mb-0'),
				Column('programa', css_class='form-group col-md-3 mb-0'),
				Column('startdate', css_class='form-group col-md-3 mb-0'),
				Column('enddate', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('partisipasaunM', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunF', css_class='form-group col-md-3 mb-0'),
				Column('totalTekniku', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunP', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('montanteOsanAlokasaun', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-5 mb-0'),
				Column('image', css_class='form-group col-md-3 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class ImplementasaunForm1(forms.ModelForm):
	startdate = forms.DateField(label='Data Hahu Implementasaun', widget=DateInput())
	enddate = forms.DateField(label='Data Remata Implementasaun', widget=DateInput())
	class Meta:
		model = Implementasaun
		fields = ['programa','montanteOsanAlokasaun','startdate','enddate','image','description','survey','partisipasaunF','totalTekniku','partisipasaunM','partisipasaunP']
		exclude = ['municipality','administrativepost','village','user_created','hashed','date_created','statusImplementasaun','rejected_info','is_rejected']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		implementedSurvey = Implementasaun.objects.all().values_list('survey__id',flat=True)
		usedSurveyID = Survey.objects.filter(id__in=implementedSurvey).values_list('id', flat=True)
		self.fields['survey'].queryset = Survey.objects.exclude(id__in=usedSurveyID).filter(is_approved=True)
		self.fields['description'].widget.attrs['rows'] = 2
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('survey', css_class='form-group col-md-3 mb-0'),
				Column('programa', css_class='form-group col-md-3 mb-0'),
				Column('startdate', css_class='form-group col-md-3 mb-0'),
				Column('enddate', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('partisipasaunM', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunF', css_class='form-group col-md-3 mb-0'),
				Column('totalTekniku', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunP', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('montanteOsanAlokasaun', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-5 mb-0'),
				Column('image', css_class='form-group col-md-3 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class ImplementasaunForm2(forms.ModelForm):
	startdate = forms.DateField(label='Data Hahu Implementasaun', widget=DateInput())
	enddate = forms.DateField(label='Data Remata Implementasaun', widget=DateInput())
	class Meta:
		model = Implementasaun
		fields = ['programa','montanteOsanAlokasaun','startdate','enddate','image','description','village','survey','partisipasaunF','totalTekniku','partisipasaunM','partisipasaunP']
		exclude = ['municipality','administrativepost','user_created','hashed','date_created','statusImplementasaun','rejected_info','is_rejected']

	def __init__(self, *args, **kwargs):
		administrativepost = kwargs.pop('administrativepost',None)
		super().__init__(*args, **kwargs)
		implementedSurvey = Implementasaun.objects.all().values_list('survey__id',flat=True)
		usedSurveyID = Survey.objects.filter(id__in=implementedSurvey).values_list('id', flat=True)
		self.fields['survey'].queryset = Survey.objects.exclude(id__in=usedSurveyID).filter(is_approved=True)
		self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost.id)
		self.fields['description'].widget.attrs['rows'] = 2
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('survey', css_class='form-group col-md-12 mb-0'),
				Column('programa', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				Column('startdate', css_class='form-group col-md-3 mb-0'),
				Column('enddate', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('partisipasaunM', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunF', css_class='form-group col-md-3 mb-0'),
				Column('totalTekniku', css_class='form-group col-md-3 mb-0'),
				Column('partisipasaunP', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('montanteOsanAlokasaun', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-5 mb-0'),
				Column('image', css_class='form-group col-md-3 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

