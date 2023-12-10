from django import forms

product_category = [(1, "Food"), (2, "Snacks"), (3, "Drinks"), (4, "Hardware")]


class Product(forms.Form):

    pName = forms.CharField(label="Name", label_suffix="-")
    pCategory = forms.ChoiceField(choices=product_category, label="Category", label_suffix="-")
    pDescription = forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    pRating = forms.IntegerField(label="Rating", label_suffix="=")
