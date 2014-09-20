from django.contrib import admin

# Register your models here.

from django import forms

from models import JsonTest
from splitjson.widgets import SplitJSONWidget


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
