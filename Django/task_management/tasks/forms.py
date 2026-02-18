from django import forms
from tasks.models import Task

# django form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Task title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    # img= forms.ImageField()
    due_date= forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Assigned To')
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        print(employees)
        
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in employees]



class StyleFormMixin:
    """
    Mixin to apply Tailwind styling automatically
    """

    default_classes = (
        "w-full border border-gray-300 rounded-lg p-2 "
        "focus:outline-none focus:ring-2 focus:ring-rose-500"
    )

    textarea_classes = default_classes + " h-40"

    checkbox_classes = (
        "h-4 w-4 text-rose-600 border-gray-300 rounded "
        "focus:ring-rose-500"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": self.textarea_classes,
                    "placeholder": f"Enter {field.label.lower()}"
                })

            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": self.checkbox_classes
                })

            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": self.default_classes
                })

            else:
                field.widget.attrs.update({
                    "class": self.default_classes,
                    "placeholder": f"Enter {field.label.lower()}"
                })


    
# Django model form
class TaskModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']

        widgets = {
            'due_date': forms.SelectDateWidget(),
            'assigned_to': forms.CheckboxSelectMultiple(),
        }