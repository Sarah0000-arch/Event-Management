from django import forms
from events.models import Event, Category,Participant
class StyledFormMixin:
    default_classes = "block border-2 border-gray-300 p-3 w-full rounded-lg shadow-md focus:outline-none focus:border-rose-500 focus:ring-rose-500"
    def apply_styled_widget(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                print("inside textinput")
                field.widget.attrs.update({
                    'class': self.default_classes,
                    "placeholder":f" Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                print("inside textarea")
                field.widget.attrs.update({
                    'class': self.default_classes,
                    "placeholder":f" Enter {field.label.lower()}",
                    'rows':5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("inside date")
                field.widget.attrs.update({
                    'class': "border-2 border-gray-300 p-3 rounded-lg shadow-md focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                'class': self.default_classes,
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("inside checkbox")
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                print("inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })

class EventModelForm(StyledFormMixin, forms.ModelForm):
        class Meta:
            model= Event
            fields= '__all__'
            widgets = {
                'date': forms.SelectDateWidget(),
                'time': forms.TimeInput(attrs={'type': 'time'}),
                'participants': forms.CheckboxSelectMultiple()
            }
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)
             self.apply_styled_widget()

class CategoryModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model= Category
        fields= ['name','description']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.apply_styled_widget()

class ParticipantModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model= Participant
        fields= ['name','email']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.apply_styled_widget()