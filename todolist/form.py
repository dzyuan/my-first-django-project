


class ConotactForm(ModelForm):
    class Meta:
        model = Contact
        field = ('title','content') 