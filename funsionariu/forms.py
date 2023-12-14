from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from custom.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class FunsionariuPostuForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','areamunicipality','areaadministrativepost','nu_telefone','email','seksu','pozisaun']
		exclude = ['user_created','hashed','date_created','aldeia','areavillage','tipu_f']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		self.fields['areamunicipality'].queryset = Municipality.objects.all()
		self.fields['areaadministrativepost'].queryset = AdministrativePost.objects.none()
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

		if 'areamunicipality' in self.data:
			try:
				areamunicipality = int(self.data.get('areamunicipality'))
				self.fields['areaadministrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=areamunicipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['areaadministrativepost'].queryset = self.instance.areamunicipality.administrativepost_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('areamunicipality', css_class='form-group col-md-6 mb-0'),
				Column('areaadministrativepost', css_class='form-group col-md-6 mb-0'),
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

class FunsionariuDiretorForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','nu_telefone','email','seksu','pozisaun']
		exclude = ['user_created','hashed','date_created','aldeia','areavillage','tipu_f']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
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
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
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

class FunsionariuEIPForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','areamunicipality','areaadministrativepost','areavillage','nu_telefone','email','seksu','pozisaun','tipu_f']
		exclude = ['user_created','hashed','date_created','aldeia','tipu_f']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
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

		if 'areamunicipality' in self.data:
			try:
				areamunicipality = int(self.data.get('areamunicipality'))
				self.fields['areaadministrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=areamunicipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['areaadministrativepost'].queryset = self.instance.areamunicipality.administrativepost_set.order_by('name')

		if 'areaadministrativepost' in self.data:
			try:
				areaadministrativepost = int(self.data.get('areaadministrativepost'))
				self.fields['areavillage'].queryset = Village.objects.filter(administrativepost__id=areaadministrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['areavillage'].queryset = self.instance.areaadministrativepost.village_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('areamunicipality', css_class='form-group col-md-4 mb-0'),
				Column('areaadministrativepost', css_class='form-group col-md-4 mb-0'),
				Column('areavillage', css_class='form-group col-md-4 mb-0'),
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

class UpdateFunsionariuForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','nu_telefone','email','seksu','pozisaun']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
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
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-4 mb-0'),
				Column('email', css_class='form-group col-md-4 mb-0'),
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

