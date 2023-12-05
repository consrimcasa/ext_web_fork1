from datetime import date
import datetime
from django import forms
# from app1.models import Article

from .models import *
# from django.contrib.auth import Userimport Layout, Field, Div
from django import forms
from django.utils.translation import ugettext_lazy as _
# from tinymce.widgets import TinyMCE

class DateInput(forms.DateInput):
    input_type = 'date'


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         # fields = ['montant_deposee', 'date_de_depo', 'deposit_type', 'dette', 'client', 'employee', 'description']
        
#         fields = '__all__'
#         article_content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
#         widgets={
#             'published_date': DateInput()
#         } 


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         widgets = {
#             # 'published_date': DateInput(),
#             # 'content': TinyMCE(attrs={'cols': 46, 'rows': 30}),
#             # 'content': TinyMCE(),
#             'content': forms.Textarea(attrs={'id': 'myTextarea'}),
#         }