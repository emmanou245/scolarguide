from django import forms


class ValidateUserForm(forms.Form):
    name_psl = forms.CharField(max_length=15)
    sec_name_psl = forms.CharField(max_length=15)
    genre = forms.CharField(max_length=7)
    password_psl = forms.CharField(max_length=8)
    cpassword = forms.CharField(max_length=8)
    email_psl = forms.CharField(max_length=76)
    img_psl = forms.ImageField(max_length=150)
    date_naiss = forms.CharField(max_length=10)
    mat_number_psl = forms.CharField(max_length=10)
    cat_psl = forms.CharField(max_length=2)
    fonc_grd_psl = forms.CharField(max_length=2)
    pl_h_dip_pro = forms.CharField(max_length=13)
    pl_h_dip_aca = forms.CharField(max_length=13)
    anciennete_svr = forms.CharField(max_length=2)
    old = forms.CharField(max_length=9)
    status = forms.CharField(max_length=15)

    def clean(self):
        cleaned_data = super(ValidateUserForm, self).clean()
        name_psl = cleaned_data.get("name_psl")
        sec_name_psl = cleaned_data.get("sec_name_psl")
        genre = cleaned_data.get("genre")
        password_psl = cleaned_data.get("password_psl")
        cpassword = cleaned_data.get("cpassword")
        email_psl = cleaned_data.get("email_psl")
        img_psl = cleaned_data.get("img_psl")
        date_naiss = cleaned_data.get("date_naiss")
        mat_number_psl = cleaned_data.get("mat_number_psl")
        cat_psl = cleaned_data.get("cat_psl")
        fonc_grd_psl = cleaned_data.get("fonc_grd_psl")
        pl_h_dip_pro = cleaned_data.get("pl_h_dip_pro")
        pl_h_dip_aca = cleaned_data.get("pl_h_dip_aca")
        anciennete_svr = cleaned_data.get("anciennete_svr")
        old = cleaned_data.get("old")
        status = cleaned_data.get("status")
        # Vérifie que les deux champs sont valides
        if name_psl and sec_name_psl and genre and password_psl and cpassword and email_psl and img_psl and date_naiss \
                and mat_number_psl and cat_psl and fonc_grd_psl and pl_h_dip_pro and pl_h_dip_aca and pl_h_dip_aca \
                and anciennete_svr and old and status:
            if password_psl != cpassword:
                raise forms.ValidationError("Revoir le mot de passe (!)")
        return cleaned_data
