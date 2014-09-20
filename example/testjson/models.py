from django.db import models
from django.contrib import admin
from django import forms

# Create your models here.

from splitjson.widgets import SplitJSONWidget

class JsonTest(models.Model):
    test = models.TextField(blank=True, null=True, default='{"t1":""}')
    test2 = models.TextField(blank=True, null=True, default='{"t2":""}')

class JsonTestAdminForm(forms.ModelForm):
    test = forms.CharField(widget=SplitJSONWidget(attrs={'class': 'json-response-type', 'size': '40'},
        debug=True),
        initial={'data1': ''})
    test2 = forms.CharField(widget=SplitJSONWidget(attrs={'class': 'json-response-type', 'size': '40'}, 
        debug=True),
        initial={'data2': ''})

class JsonTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'test',)
    form = JsonTestAdminForm

admin.site.register(JsonTest, JsonTestAdmin)

