from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    name_rgn = models.CharField(max_length=17)
    abbrev_rgn = models.CharField(max_length=2)
    desc_rgn = models.TextField()
    img_region = models.ImageField(upload_to="images/regions")
    last_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_rgn


class Department(models.Model):
    name_dep = models.CharField(max_length=17)
    desc_dep = models.TextField()
    img_dep = models.ImageField(upload_to="images/departments")
    last_modify_dep = models.DateTimeField(auto_now=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_dep


class Arrondissement(models.Model):
    name_arr = models.CharField(max_length=17)
    code_arr = models.CharField(max_length=4)
    desc_arr = models.TextField()
    img_arr = models.ImageField(upload_to="images/arrondissements")
    longitude_arr = models.FloatField(max_length=8)
    latitude_arr = models.FloatField(max_length=8)
    last_modify_arr = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_arr


class Order(models.Model):
    name_ord = models.CharField(max_length=13)
    abbrv_ord = models.CharField(max_length=4)
    num_ord = models.CharField(max_length=1)

    def __str__(self):
        return self.name_ord


class School(models.Model):
    name_sch = models.CharField(max_length=31)
    system_sch = models.CharField(max_length=13)
    cycle_complete = models.CharField(max_length=13)
    exit_apee_sch = models.CharField(max_length=3)
    regime_sch = models.CharField(max_length=13)
    longitude_sch = models.FloatField(max_length=8)
    latitude_sch = models.FloatField(max_length=8)
    altitude_sch = models.FloatField(max_length=8)
    addr_sch = models.TextField(max_length=53)
    zone_sch = models.CharField(max_length=8)
    code_sch = models.CharField(max_length=12)
    desc_sch = models.TextField()
    img_sch = models.ImageField(upload_to="images/schools")
    last_modify_sch = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_sch


class Cycle(models.Model):
    name_ccl = models.CharField(max_length=31)
    desc_ccl = models.TextField()
    img_ccl = models.ImageField(upload_to="images/cycles")
    last_modify_ccl = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ccl


class Offer(models.Model):
    edition_year = models.CharField(max_length=10)
    drink_water = models.CharField(max_length=22)
    energy = models.CharField(max_length=13)
    internet = models.CharField(max_length=22)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)

    def __str__(self):
        return self.edition_year+" - "+self.school.name_sch+" - "+self.cycle.name_ccl


class LetterAl(models.Model):
    name_lta = models.CharField(max_length=1)
    num_lta = models.CharField(max_length=2)

    def __str__(self):
        return self.name_lta


class Infrastructure(models.Model):
    name_inf = models.CharField(max_length=62)
    state_inf = models.CharField(max_length=13)
    status_inf = models.CharField(max_length=13)
    abbrv_inf = models.CharField(max_length=7)
    desc_inf = models.TextField(max_length=7)
    capacity = models.IntegerField()
    img_inf = models.ImageField(upload_to="images/classes")
    last_modify_inf = models.DateTimeField(auto_now=True)
    class_or_inf = models.CharField(max_length=1)
    letter = models.ForeignKey(LetterAl, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    total_girls = models.IntegerField()
    total_boys = models.IntegerField()
    total_tables = models.IntegerField()
    total_handic = models.IntegerField()

    def __str__(self):
        return self.abbrv_inf+" - "+self.letter.name_lta+" - "+self.school.name_sch


class Sex(models.Model):
    name_sex = models.CharField(max_length=8)
    char = models.CharField(max_length=1)

    def __str__(self):
        return self.name_sex


class Detail(models.Model):
    year_dtl = models.CharField(max_length=9)
    tt_win = models.CharField(max_length=2)
    tt_abd = models.CharField(max_length=2)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)
    handic_m = models.CharField(max_length=2)
    handic_v = models.CharField(max_length=2)
    handic_a = models.CharField(max_length=2)
    student_sp1 = models.CharField(max_length=2)
    student_sp2 = models.CharField(max_length=2)
    student_sp3 = models.CharField(max_length=2)
    depla = models.CharField(max_length=2)
    refug = models.CharField(max_length=2)
    ss_acte = models.CharField(max_length=2)

    def __str__(self):
        return self.year_dtl+" - "+self.infrastructure.name_inf+" - "+self.infrastructure.letter.name_lta+" - "+self.sex.name_sex+" - "+self.infrastructure.school.name_sch


class OldClass(models.Model):
    odl_class = models.CharField(max_length=8)
    number_class = models.CharField(max_length=2)

    def __str__(self):
        return self.odl_class


class StatusPsl(models.Model):
    label_stp = models.CharField(max_length=13)
    abbrev_stp = models.CharField(max_length=6)
    abr_stp = models.CharField(max_length=125)

    def __str__(self):
        return self.label_stp


class Personal(models.Model):
    name_psl = models.CharField(max_length=15)
    sec_name_psl = models.CharField(max_length=15)
    genre = models.CharField(max_length=7)
    password_psl = models.CharField(max_length=8)
    email_psl = models.CharField(max_length=76)
    img_psl = models.ImageField(upload_to="images/personals")
    date_naiss = models.CharField(max_length=10)
    mat_number_psl = models.CharField(max_length=10)
    cat_psl = models.CharField(max_length=2)
    fonc_grd_psl = models.CharField(max_length=2)
    pl_h_dip_pro = models.CharField(max_length=13)
    pl_h_dip_aca = models.CharField(max_length=13)
    anciennete_svr = models.CharField(max_length=2)
    last_activity = models.DateTimeField(auto_now=True)
    last_modify_pers = models.DateTimeField(auto_now=True)
    old = models.ForeignKey(OldClass, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusPsl, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_psl


class Appart(models.Model):
    fonction_psl = models.CharField(max_length=15)
    year_affect = models.CharField(max_length=10)
    year_start_srv = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    last_modify_apt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fonction_psl