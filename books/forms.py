from django import forms

class SearchForm(forms.Form):
  search_input=forms.CharField(max_length=100, required=True , label= "",
                               widget=forms.TextInput(attrs={"placeholder":"Search By Book Name",
                                                             "id":"search"}),)
  

class AuthorSearchForm(forms.Form):
  search_input=forms.CharField(max_length=100, required=True , label= "",
                               widget=forms.TextInput(attrs={"placeholder":"Search By Author Name",
                                                             "id":"search"}),)  
  
class CategorySearchForm(forms.Form):
  search_input=forms.CharField(max_length=100, required=True , label= "",
                               widget=forms.TextInput(attrs={"placeholder":"Search By Categories Name",
                                                             "id":"search"}),)   