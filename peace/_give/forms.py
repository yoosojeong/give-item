from django import forms
from .models import ItemPostModel

class ItemPostForm(forms.ModelForm):
    class Meta:
        model = ItemPostModel
        fields = ('images', 'type_item', 'state_item', 'location', 'title', 'cost', 'contents', 'amount', 'tags')

    def __init__(self, *args, **kwargs):

        super(ItemPostForm, self).__init__(*args, **kwargs)
    
        self.fields['images'].widget = forms.FileInput(attrs={
            'class': 'form-control form-control-sm mb-1',
            'name': 'title',
            'autocomplete': 'off',
            'required':'requireds'})
        self.fields['type_item'].widget = forms.Select(
            attrs={
            'class': 'form-control form-control-sm mb-1',
            'name': 'gugun'},
            choices=ItemPostModel.TYPE_CHOICES
        )
        self.fields['state_item'].widget = forms.Select(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'type'},
            choices=ItemPostModel.STATE_CHOICES
        )
        self.fields['location'].widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'gender'},
        )
        self.fields['title'].widget = forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'cost',
                'autocomplete': 'off',
                'placeholder':'예) 100000'},
        )
        self.fields['cost'].widget = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'period',
                'autocomplete': 'off',
                'placeholder': '예) 15'},
        )
        self.fields['contents'].widget = forms.Textarea(
            attrs={
                'id': 'deadline_datepicker',
                'class': 'form-control form-control-sm mb-1',
                'name': 'deadline',
                'autocomplete': 'off'},
        )
        self.fields['amount'].widget = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'content',
                'autocomplete': 'off'},
        )
        self.fields['tags'].widget = forms.TextInput(
            attrs={
                'id': 'start_datepicker',
                'class': 'form-control form-control-sm mb-1',
                'name': 'start_at',
                'autocomplete': 'off'},
        )