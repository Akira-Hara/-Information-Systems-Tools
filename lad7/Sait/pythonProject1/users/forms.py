from django import forms

# объявляем форму с именем NameForm
# принадлежащую классу Form
class NameForm(forms.Form):
    # форма имеет одно поле, строкового типа
    # имеет подпись - label
    # имеет максимальную длину 100 символов
    user_name = forms.CharField(label='The username contains:',
                                required=False,
                                max_length=100)

    user_name_2 = forms.CharField(label='The username contains:',
                                  required=False,
                                  max_length=100)

    user_name_3 = forms.CharField(label='The username contains:',
                                  required=False,
                                  max_length=100)