from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        # Vérifi e que les deux champs sont valides
        if username and password:
            if password != 'sesame' or username != 'pierre@lxs.be':
                raise forms.ValidationError("Nom d'utilisateur ou mot de passe érroné (!)")
        return cleaned_data
