from .models import DraftResult, Expansion
from django import forms
from django.core.validators import FileExtensionValidator
from .validators import FileSizeValidator, FileTypeValidator

class DraftResultForm(forms.ModelForm):
    expansion = forms.ModelChoiceField(queryset=Expansion.objects.order_by('-release_date'))
    deck_title = forms.CharField(required=False)
    class Meta:
        model = DraftResult
        fields = [
            "date",
            "expansion",
            "best_of",
            "deck_title",
            "nb_wins",
            "nb_losses",
            "colors",
            ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ImportResultsForm(forms.Form):
    file = forms.FileField(validators=[
        FileExtensionValidator(['xlsx', 'xls']),
        FileSizeValidator,
        FileTypeValidator(content_types=('Microsoft Excel 2007+', 'Microsoft Excel 2003', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))
        ])