import datetime
import folium

import numpy as np
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from . import models
from .forms import ValidateUserForm
from .models import Region, Department, Arrondissement, School, Offer, Infrastructure, Detail, Personal, StatusPsl, \
    OldClass, Appart, Order, Cycle, LetterAl, Sex


def error403(request):
    dhb_context = {'messageErr': 'CETTE RESSOURCE REQUIèRE UNE AUTHENTIFICATION !'}
    return render(request, "administrator/error-403.html", dhb_context)


def dashbordAdm(request):
    if request.user.is_authenticated:
        dhb_context = {'title': 'PANEL D\'ADMINISTRATION'}
        return render(request, "administrator/index.html", dhb_context)
    else:
        return redirect(error403)


def manageRgn(request):
    if request.user.is_authenticated:
        list_regions = Region.objects.all()
        if len(request.POST) > 0:
            if 'name_rgn' not in request.POST or 'abbrev_rgn' not in request.POST or 'img_rgn' not in request.POST:
                error = "Veuillez remplir correctement le formulaire."
            else:
                new_region = Region(name_rgn=request.POST['name_rgn'], abbrev_rgn=request.POST['abbrev_rgn'],
                                    desc_rgn="A modifier", img_region='images/regions/' + request.POST['img_rgn'],
                                    last_modify=datetime.date.today())

                new_region.save()
                rgn_context = {"list_regions": list_regions, 'title': 'LISTE DES REGIONS'}
                return render(request, "administrator/rgn_manage.html", rgn_context)
        rgn_context = {"list_regions": list_regions, 'title': 'LISTE DES REGIONS'}

        return render(request, "administrator/rgn_manage.html", rgn_context)
    else:
        return redirect(error403)


def listRgn(request):
    if request.user.is_authenticated:
        list_regions = Region.objects.all()
        rgn_context = {"list_regions": list_regions, 'title': 'GESTIONS DES REGIONS'}
        return render(request, "administrator/rgn_manage.html", rgn_context)
    else:
        return redirect(error403)


def listSch(request):
    if request.user.is_authenticated:

        personals = Personal.objects.all()
        rgn_context = {"personals": personals, 'title': 'GESTIONS DES PERSONNELS',
                       'sub_title': 'Liste du personnel enregistré '}
        return render(request, "administrator/sch_manage.html", rgn_context)
    else:
        return redirect(error403)


def precisionRgn(request, id_region):
    if request.user.is_authenticated:
        departments = Department.objects.filter(region=id_region)
        region = Region.objects.get(id=id_region)
        dep_rgn_context = {"departments": departments, 'title': 'GERER LA REGION : ' + region.name_rgn,
                           'sub_title': 'Liste des départements de la région',
                           'region': region
                           }
        return render(request, 'administrator/rgn_precision.html', dep_rgn_context)
    else:
        return redirect(error403)


def deleteRgn(request, id_region):
    if request.user.is_authenticated:
        region = Region.objects.get(id=id_region)
        region.delete()
        message = 'Region supprimer avec succes'
        list_regions = Region.objects.all()
        rgn_context = {"list_regions": list_regions, 'title': 'GESTIONS DES REGIONS', 'message': message}
        return redirect(listRgn)
    else:
        return redirect(error403)


def precisionDpt(request, id_dep):
    if request.user.is_authenticated:

        arrondissements = Arrondissement.objects.filter(department=id_dep)
        department = Department.objects.get(id=id_dep)
        arr_dep_context = {"arrondissements": arrondissements, 'title': 'GERER LE DEPARTEMENT : ' + department.name_dep,
                           'sub_title': 'Liste des arrondissements du département ', 'department': department}
        return render(request, 'administrator/dep_precision.html', arr_dep_context)
    else:
        return redirect(error403)


def precisionArr(request, id_arr):
    if request.user.is_authenticated:
        personals = Personal.objects.filter(fonc_grd_psl='EN')
        schools = School.objects.filter(arrondissement=id_arr)
        arrondissement = Arrondissement.objects.get(id=id_arr)
        arrs = Arrondissement.objects.all()
        orders = Order.objects.all()
        apparts = Appart.objects.filter(fonction_psl='Proviseur')
        sch_arr_context = {"schools": schools, "arrondissement": arrondissement, 'orders': orders,
                           'arrs': arrs, 'title': 'GERER L\'ARRONDISSEMENT : ' + arrondissement.name_arr,
                           'apparts': apparts, 'sub_title': 'Liste des établissements de l\'arrondissement ',
                           'personals': personals}
        return render(request, 'administrator/arr_precision.html', sch_arr_context)
    else:
        return redirect(error403)


def allSchools(request):
    if request.user.is_authenticated:

        schools = School.objects.all()
        orders = Order.objects.all()
        personals = Personal.objects.filter(fonc_grd_psl='EN')
        apparts = Appart.objects.filter(fonction_psl='Proviseur')
        arrs = Arrondissement.objects.all()

        if request.method == "POST":
            school = School.objects.create(
                name_sch=request.POST['name_sch'],
                system_sch=request.POST['system_sch'],
                cycle_complete=request.POST['cycle_complete'],
                exit_apee_sch=request.POST['exit_apee_sch'],
                regime_sch=request.POST['regime_sch'],
                longitude_sch=request.POST['longitude_sch'],
                latitude_sch=request.POST['latitude_sch'],
                altitude_sch=request.POST['altitude_sch'],
                addr_sch=request.POST['addr_sch'],
                zone_sch=request.POST['zone_sch'],
                code_sch=request.POST['code_sch'],
                desc_sch=request.POST['desc_sch'],
                img_sch="/images/schools/" + request.POST['img_sch'],
                last_modify_sch=datetime.date.today(),
                order=Order.objects.get(id=request.POST['order']),
                arrondissement=Arrondissement.objects.get(id=request.POST['arrondissement'])
            )
            school.save()
            message = 'Etablissement enregistré avec succes !'
            sch_arr_context = {'message': message, 'apparts': apparts, "schools": schools,
                               'title': 'GESTION EXTERNE DES ETABLISSEMENTS ', 'sub_title':'Liste des établissements enregistrés', 'orders': orders,
                               'arrs': arrs, 'personals': personals}
            return render(request, 'administrator/arr_precision.html', sch_arr_context)

        sch_arr_context = {'apparts': apparts, "schools": schools, 'title': 'GESTION EXTERNE DES ETABLISSEMENTS ', 'orders': orders,
                           'arrs': arrs, 'personals': personals, 'sub_title':'Liste des établissements enregistrés',}
        return render(request, 'administrator/arr_precision.html', sch_arr_context)
    else:
        return redirect(error403)


def updateSchool(request):
    if request.user.is_authenticated:
        schools = School.objects.all()
        orders = Order.objects.all()
        personals = Personal.objects.filter(fonc_grd_psl='EN')
        arrs = Arrondissement.objects.all()
        apparts = Appart.objects.all()

        if request.method == "POST":
            school = School.objects.get(id=request.POST['id_sch'])
            school.name_sch = request.POST['name_sch']
            school.system_sch = request.POST['system_sch']
            school.cycle_complete = request.POST['cycle_complete']
            school.exit_apee_sch = request.POST['exit_apee_sch']
            school.regime_sch = request.POST['regime_sch']
            school.longitude_sch = request.POST['longitude_sch']
            school.latitude_sch = request.POST['latitude_sch']
            school.altitude_sch = request.POST['altitude_sch']
            school.addr_sch = request.POST['addr_sch']
            school.zone_sch = request.POST['zone_sch']
            school.code_sch = request.POST['code_sch']
            school.desc_sch = request.POST['desc_sch']
            school.img_sch = "/images/schools/" + request.POST['img_sch']
            school.last_modify_sch = datetime.date.today()
            school.order = Order.objects.get(id=request.POST['order'])
            school.arrondissement = Arrondissement.objects.get(id=request.POST['arrondissement'])

            school.save()

            message = 'Etablissement enregistré avec succes !'
            sch_arr_context = {'message': message, 'apparts': apparts, "schools": schools, 'title': 'LES ETABLISSEMENTS ',
                               'orders': orders, 'arrs': arrs, 'personals': personals}
            return render(request, 'administrator/arr_precision.html', sch_arr_context)

        school = School.objects.get(id=request.GET['id_sch'])
        sch_arr_context = {'apparts': apparts, "school": school,
                           'title': "Modification de l'établissement - " + school.name_sch,
                           'orders': orders, 'arrs': arrs, 'personals': personals}
        return render(request, 'administrator/update_school.html', sch_arr_context)
    else:
        return redirect(error403)


def search(request):
    if request.user.is_authenticated:

        query = request.GET["search"]
        result_object = School.objects.filter(name_sch__icontains=query)
        # result_object = result_object.append(School.objects.filter(system_sch__icontains=query))
        rst_srh_context = {'title': 'RESULTATS DE LA RECHERCHE LIEE A : ' + query, 'result_object': result_object}
        return render(request, 'administrator/search_result.html', rst_srh_context)
    else:
        return redirect(error403)


def inSchool(request, id_sch):
    if request.user.is_authenticated:
        school = School.objects.get(id=id_sch)
        infrastructures = Infrastructure.objects.filter(school=id_sch, class_or_inf='1')
        classes = Infrastructure.objects.filter(school=id_sch, class_or_inf='0')
        offers = Offer.objects.filter(school=id_sch)
        apparts = Appart.objects.filter(school=id_sch)
        sch_context = {'title': 'GESTION INTERNE DE L\'ECOLE : ' + school.name_sch, 'infrastructures': infrastructures,
                       'offers': offers, 'apparts': apparts, 'classes': classes}
        return render(request, 'administrator/in_school.html', sch_context)
    else:
        return redirect(error403)


def inClass(request, id_cls):
    if request.user.is_authenticated:
        sex = "Masculin"
        this_class = Infrastructure.objects.get(id=id_cls)
        this_cycle = Cycle.objects.get(id=this_class.cycle.id)
        this_school = School.objects.get(id=this_class.school.id)
        this_offer = Offer.objects.filter(school=this_school)
        details = Detail.objects.filter(infrastructure=this_class)
        cls_context = {'title': 'GESTION INTERNE DE L\'ECOLE : ' + this_school.name_sch, 'details': details,
                       'this_school': this_school, 'this_cycle': this_cycle, 'this_class': this_class,
                       'this_offer': this_offer, 'sex': sex, 'id_cls': id_cls}
        return render(request, 'administrator/clss_precision.html', cls_context)
    else:
        return redirect(error403)


def submitStatClass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            school = School.objects.get(id=request.POST['id_sch'])
            infrastructures = Infrastructure.objects.filter(school=school, class_or_inf='1')
            classes = Infrastructure.objects.filter(school=school, class_or_inf='0')
            offers = Offer.objects.filter(school=school)
            apparts = Appart.objects.filter(school=school)
            classe = Infrastructure.objects.get(id=request.POST['id_cls'])
            details = Detail.objects.filter(infrastructure=classe)

            for detail in details:
                if Detail.objects.filter(id=request.POST['id_dtl'+str(detail.id)],
                                         sex=Sex.objects.get(id=2)):
                    detailF = Detail.objects.get(id=request.POST['id_dtl'+str(detail.id)])
                    detailF.tt_win = request.POST[str(detail.tt_win)+'Fwin']
                    detailF.tt_abd = request.POST[str(detail.tt_abd)+'Fabd']
                    detailF.infrastructure = classe
                    detailF.handic_m = request.POST[str(detail.handic_m)+'Fm']
                    detailF.handic_a = request.POST[str(detail.handic_a)+'Fa']
                    detailF.handic_v = request.POST[str(detail.handic_v)+'Fv']

                    detailF.student_sp1 = request.POST[str(detail.student_sp1) + 'Fstudent_sp1']
                    detailF.student_sp2 = request.POST[str(detail.student_sp2) + 'Fstudent_sp2']
                    detailF.student_sp3 = request.POST[str(detail.student_sp3) + 'Fstudent_sp3']

                    detailF.depla = request.POST[str(detail.depla)+'Fdepla']
                    detailF.refug = request.POST[str(detail.refug)+'Frefug']
                    detailF.ss_acte = request.POST[str(detail.ss_acte)+'Facte']

                    detailF.save()

                if Detail.objects.filter(id=request.POST['id_dtl'+str(detail.id)],
                                         sex=Sex.objects.get(id=1)):
                    detailG = Detail.objects.get(id=request.POST['id_dtl'+str(detail.id)])
                    detailG.tt_win = request.POST[str(detail.tt_win)+'Gwin']
                    detailG.tt_abd = request.POST[str(detail.tt_abd)+'Gabd']
                    detailG.infrastructure = classe
                    detailG.handic_m = request.POST[str(detail.handic_m)+'Gm']
                    detailG.handic_a = request.POST[str(detail.handic_a)+'Ga']
                    detailG.handic_v = request.POST[str(detail.handic_v)+'Gv']

                    detailG.student_sp1 = request.POST[str(detail.student_sp1) + 'Gstudent_sp1']
                    detailG.student_sp2 = request.POST[str(detail.student_sp2) + 'Gstudent_sp2']
                    detailG.student_sp3 = request.POST[str(detail.student_sp3) + 'Gstudent_sp3']

                    detailG.depla = request.POST[str(detail.depla) + 'Gdepla']
                    detailG.refug = request.POST[str(detail.refug) + 'Grefug']
                    detailG.ss_acte = request.POST[str(detail.ss_acte) + 'Gacte']

                    detailG.save()

            sch_context = {'title': 'GESTION INTERNE DE L\'ECOLE : ' + school.name_sch,
                                   'infrastructures': infrastructures, 'offers': offers,
                                   'apparts': apparts, 'classes': classes}
            return render(request, 'administrator/in_school.html', sch_context)

    else:
        return redirect(error403)


def manageCoursesClass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            school = School.objects.get(id=request.POST['id_sch'])
            letters = LetterAl.objects.all()
            offres = Offer.objects.filter(school=request.POST['id_sch'])
            classes = Infrastructure.objects.filter(school=request.POST['id_sch'], class_or_inf='0')
            sess_context = {'title': 'GESTION EXTERNE DES CLASSES DE : ' + school.name_sch,
                            'school': school, 'classes': classes, 'letters': letters, 'offres': offres}
            return render(request, 'administrator/in_courses_class.html', sess_context)

    else:
        return redirect(error403)


def manageSession(request):
    if request.user.is_authenticated:
        schools = School.objects.all()
        if request.method == "POST":
            school = School.objects.get(id=request.POST['id_sch'])
            classes = Infrastructure.objects.filter(school=request.POST['id_sch'], class_or_inf='0')
            sess_context = {'title': 'GESTION INTERNE DES SESSIONS SCOLAIRES: ' + school.name_sch,
                            'school': school, 'classes': classes}
            return render(request, 'administrator/in_sessions.html', sess_context)

        if request.GET['id_sch'] is not None:
            school = School.objects.get(id=request.GET['id_sch'])
            infrastructures = Infrastructure.objects.filter(school=request.GET['id_sch'], class_or_inf='1')
            classes = Infrastructure.objects.filter(school=request.GET['id_sch'], class_or_inf='0')
            offers = Offer.objects.filter(school=request.GET['id_sch'])
            apparts = Appart.objects.filter(school=request.GET['id_sch'])

            for classe in classes:
                if Infrastructure.objects.filter(name_inf=request.GET[classe.name_inf]):
                    detailF = Detail.objects.create(
                        year_dtl='20' + str(request.GET["inf_ann"]) + '-20' + str(request.GET["sup_ann"]),
                        tt_win=0, tt_abd=0, sex=Sex.objects.get(char='F'), infrastructure=classe,
                        handic_m=0, handic_v=0, handic_a=0, student_sp1=0, student_sp2=0, student_sp3=0,
                         depla=0, refug=0, ss_acte=0
                    )
                    detailF.save()

                    detailH = Detail.objects.create(
                        year_dtl='20' + str(request.GET["inf_ann"]) + '-20' + str(request.GET["sup_ann"]),
                        tt_win=0, tt_abd=0, sex=Sex.objects.get(char='M'), infrastructure=classe,
                        handic_m=0, handic_v=0, handic_a=0, student_sp1=0, student_sp2=0, student_sp3=0,
                         depla=0, refug=0, ss_acte=0
                    )
                    detailH.save()

                    classe.total_girls = request.GET['total_girls' + str(classe.id)]
                    classe.total_boys = request.GET['total_boys' + str(classe.id)]
                    classe.total_boys = request.GET['total_boys' + str(classe.id)]
                    classe.total_tables = request.GET['total_tables' + str(classe.id)]
                    classe.total_handic = request.GET['total_handic' + str(classe.id)]

                    classe.capacity = int(classe.total_girls) + int(classe.total_boys)

                    classe.save()

            sch_context = {'title': 'GESTION INTERNE DE L\'ECOLE : ' + school.name_sch,
                                   'infrastructures': infrastructures, 'offers': offers,
                                   'apparts': apparts, 'classes': classes}
            return render(request, 'administrator/in_school.html', sch_context)

        sess_context = {'title': 'GESTION INTERNE DES SESSIONS SCOLAIRES: ', 'schools': schools}
        return render(request, 'administrator/gestion_dep_etab.html', sess_context)
    else:
        return redirect(error403)


def addRegion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            region = Region.objects.create(
                name_rgn=request.POST['name_rgn'],
                abbrev_rgn=request.POST['abbrev_rgn'],
                rgn_desc=request.POST['rgn_desc'],
                img_region=request.POST['img_region']
            )
            region.save()
            return redirect('dashbordAdm')
        dhb_context = {'title': 'CONNEXION'}
    else:
        return redirect(error403)


def updateRegion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            region = Region.objects.get(id=request.POST['id_rgn'])
            region.name_rgn = request.POST['name_rgn']
            region.abbrev_rgn = request.POST['abbrev_rgn']
            region.rgn_desc = request.POST['rgn_desc']
            region.img_region = request.POST['img_region']
            region.save()
            up_rgn_context = {'message': 'Modification de la région avec succès !'}
            return render(request, 'administrator/index.html', up_rgn_context)

    else:
        return redirect(error403)


def plotMap(request, id_sch):
    if request.user.is_authenticated:

        school = School.objects.get(id=id_sch)
        schools = School.objects.filter(arrondissement=school.arrondissement.id)
        arr = Arrondissement.objects.get(id=school.arrondissement.id)

        arr_circle = folium.Map(location=[arr.longitude_arr, arr.latitude_arr], zoom_start=15)
        for school in schools:
            folium.CircleMarker(school.latitude_sch,
                                popup='<i>' + school.name_sch + '</i>', tooltip=school.name_sch).add_to(arr_circle)
            #radius = prop["surface"] / 1000000
        arr_circle

        for i in schools:
            folium.Marker([i.latitude_sch, i.longitude_sch], ).add_to(m)

        arr_circle = arr_circle._repr_html_()  # updated
        context = {'my_map': arr_circle}

        plt_context = {'title': 'Localisation', 'school': school, 'context': context}
        return render(request, 'administrator/localisation.html', context)
    else:
        return redirect(error403)


def managePers(request):
    if request.user.is_authenticated:
        psl_context = {'title': 'GESTION DU PERSONNEL',
                       'personals': Personal.objects.all(),
                       'status': StatusPsl.objects.all(),
                       'schools': School.objects.all(),
                       'apparts': Appart.objects.all(),
                       'arrondissements': Arrondissement.objects.all(),
                       'olds': OldClass.objects.all()
                       }
        return render(request, 'administrator/personals.html', psl_context)
    else:
        return redirect(error403)


def modifPersF(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            psl_context = {'title': 'GESTION DU PERSONNEL',
                           'id_psl': request.POST["id_psl"],
                           'personals': Personal.objects.all(),
                           'status': StatusPsl.objects.all(),
                           'apparts': Appart.objects.all(),
                           'schools': School.objects.all(),
                           'arrondissements': Arrondissement.objects.all(),
                           'olds': OldClass.objects.all(),
                           'message': 'Modification du personnel avec succès.'
                           }
            personal = Personal.objects.get(id=request.POST["id_psl"])
            personal.name_psl = request.POST["name_psl"]
            personal.sec_name_psl = request.POST["sec_name_psl"]
            personal.genre = request.POST["genre"]
            personal.password_psl = request.POST["password_psl"]
            personal.email_psl = request.POST["email_psl"]
            personal.img_psl = 'images/personals/' + request.POST["img_psl"]
            personal.date_naiss = request.POST["date_naiss"]
            personal.mat_number_psl = request.POST["mat_number_psl"]
            personal.cat_psl = request.POST["cat_psl"]
            personal.fonc_grd_psl = request.POST["fonc_grd_psl"]
            personal.pl_h_dip_pro = request.POST["pl_h_dip_pro"]
            personal.pl_h_dip_aca = request.POST["pl_h_dip_aca"]
            personal.anciennete_svr = request.POST["anciennete_svr"]
            personal.old = OldClass.objects.get(id=request.POST["old"])
            personal.status = StatusPsl.objects.get(id=request.POST["status"])
            personal.last_activity = datetime.date.today()
            personal.last_modify_pers = datetime.date.today()

            personal.save()

            return render(request, 'administrator/personals.html', psl_context)
    else:
        return redirect(error403)


def modifPers(request, id_psl):
    if request.user.is_authenticated:
        this_psl_context = {'title': 'MODIFICATION DU PERSONNEL',
                            'this_personals': Personal.objects.get(id=id_psl),
                            'status': StatusPsl.objects.all(),
                            'schools': School.objects.all(),
                            'arrondissements': Arrondissement.objects.all(),
                            'olds': OldClass.objects.all()
                            }

        return render(request, 'administrator/update_personal.html', this_psl_context)
    else:
        return redirect(error403)


def deletePers(request, id_psl):
    if request.user.is_authenticated:
        personal = Personal.objects.get(id=id_psl)
        personal.delete()
        psl_context = {'title': 'GESTION DU PERSONNEL',
                       'personals': Personal.objects.all(),
                       'status': StatusPsl.objects.all(),
                       'schools': School.objects.all(),
                       'arrondissements': Arrondissement.objects.all(),
                       'apparts': Appart.objects.all(),
                       'olds': OldClass.objects.all(),
                       'message': 'Suppression du personnel avec succès.'
                       }
        return render(request, 'administrator/personals.html', psl_context)
    else:
        return redirect(error403)


def deleteSchool(request, id_sch):
    if request.user.is_authenticated:
        school = School.objects.get(id=id_sch)
        school.delete()
        sch_context = {'title': 'GESTION DES ETABLISSEMENTS',
                       'personals': Personal.objects.all(),
                       'status': StatusPsl.objects.all(),
                       'schools': School.objects.all(),
                       'arrondissements': Arrondissement.objects.all(),
                       'apparts': Appart.objects.all(),
                       'olds': OldClass.objects.all(),
                       'message': 'Suppression dudit établissement avec succès.'
                       }
        return render(request, 'administrator/arr_precision.html', sch_context)
    else:
        return redirect(error403)


def freeSchool(request):
    if request.user.is_authenticated:
        psl_context = {'title': 'GESTIONS DEPENDANTES / Etablissements :',
                       'personals': Personal.objects.all(),
                       'status': StatusPsl.objects.all(),
                       'schools': School.objects.all(),
                       'arrondissements': Arrondissement.objects.all(),
                       'apparts': Appart.objects.all(),
                       }
        return render(request, 'administrator/gestion_dep_etab.html', psl_context)
    else:
        return redirect(error403)


def manageApprt(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ValidateUserForm(request.POST)

            personal = Personal.objects.get(id=request.POST["id_psl"])
            school = School.objects.get(id=request.POST["id_sch"])

            appart = Appart.objects.create(
                fonction_psl=request.POST["fonction_psl"],
                year_affect='20' + request.POST["inf_aff"] + '-20' + request.POST["sup_aff"],
                year_start_srv='20' + request.POST["inf_aff"] + '-20' + request.POST["sup_aff"],
                personal=personal,
                school=school,
                last_modify_apt=datetime.date.today()
            )
            appart.save()
            apt_context = {'title': 'GESTION DES APPARTENANCES (Personnels - Etablissements)',
                           'personals': Personal.objects.all(),
                           'schools': School.objects.all(),
                           'apparts': Appart.objects.all(),
                           'message': 'Ajout de l`appartenance du personnel avec succès.'
                           }
            return render(request, 'administrator/personals.html', apt_context)

        apt_context = {'title': 'GESTION DES APPARTENANCES (Personnels - Etablissements)',
                       'personals': Personal.objects.all(),
                       'schools': School.objects.all(),
                       'apparts': Appart.objects.all(),
                       }
        return render(request, 'administrator/apparts.html', apt_context)
    else:
        return redirect(error403)


def manageOffer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ValidateUserForm(request.POST)

            cycle = Cycle.objects.get(id=request.POST["id_ccl"])
            school = School.objects.get(id=request.POST["id_sch"])

            offer = Offer.objects.create(
                edition_year='20' + request.POST["inf_aff"] + '-20' + request.POST["sup_aff"],
                internet=request.POST["internet"],
                energy=request.POST["energy"],
                drink_water=request.POST["drink_water"],
                cycle=cycle,
                school=school
            )
            offer.save()
            apt_context = {'title': 'GESTION DES OFFRES (ETABLISSEMENTS - CYCLES)',
                           'personals': Personal.objects.all(),
                           'schools': School.objects.all(),
                           'apparts': Appart.objects.all(),
                           'message': 'Ajout de l`appartenance du personnel avec succès.'
                           }
            return render(request, 'administrator/index.html', apt_context)

        apt_context = {'title': 'GESTION DES OFFRES (ETABLISSEMENTS - CYCLES)',
                       'cycles': Cycle.objects.all(),
                       'schools': School.objects.all(),
                       'apparts': Appart.objects.all(),
                       }
        return render(request, 'administrator/offers.html', apt_context)
    else:
        return redirect(error403)


def stautsPers(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            status = StatusPsl.objects.create(
                label_stp=request.POST["label_stp"],
                abr_stp=request.POST["abr_stp"],
                abbrev_stp=request.POST["abbrev_stp"]
            )
            status.save()
            apt_context = {'title': 'PANEL D"ADMINISTRATION - [Depuis les status des personnel]',
                           'status': StatusPsl.objects.all(), 'sub_title': 'Liste des status enregistrés'
                           }
            return render(request, 'administrator/status_personals.html', apt_context)

        apt_context = {'title': 'GESTION DES STATUS (PERSONNELS - MINISTERE)',
                       'status': StatusPsl.objects.all(), 'sub_title': 'Liste des status enregistrés'
                       }

        return render(request, 'administrator/status_personals.html', apt_context)
    else:
        return redirect(error403)


def updateStatus(request, id_stp):
    if request.user.is_authenticated:
            statu = StatusPsl.objects.get(id=id_stp)

            apt_context = {'title': 'PANEL D"ADMINISTRATION - [Depuis les status des personnel]',
                           'status': StatusPsl.objects.all(), 'sub_title': 'Liste des status enregistrés',
                           'statu': statu
                           }
            return render(request, 'administrator/status_personals.html', apt_context)
    else:
        return redirect(error403)


def deleteStatus(request, id_stp):
    if request.user.is_authenticated:
        status= StatusPsl.objects.get(id=id_stp)
        status.delete()
        apt_context = {'title': 'GESTION DES STATUS (PERSONNELS - MINISTERE)',
                       'status': StatusPsl.objects.all(), 'sub_title': 'Liste des status enregistrés'
                       }
        return render(request, 'administrator/status_personals.html', apt_context)
    else:
        return redirect(error403)


def allStats(request):
    if request.user.is_authenticated:
        stat_context = {'title': 'TOUTES LES STATISTIQUES',
                        'regions': Region.objects.all(),
                        'departments': Department.objects.all(),
                        'schools': School.objects.all(),
                        'arrondissements': Arrondissement.objects.all(),
                        'olds': OldClass.objects.all()}
        return render(request, 'administrator/all_stats.html', stat_context)
    else:
        return redirect(error403)


def allStatsSchools(request):
    if request.user.is_authenticated:
        stat_context = {'title': 'TOUTES LES STATISTIQUES DES ETABLISSEMENTS ENREGISTRES',
                        'sub_title': 'Liste des établissements ',
                        'orders': Order.objects.all(),
                        'sexG': Sex.objects.get(char='M'),
                        'details': Detail.objects.all(),
                        'infrastructures': Infrastructure.objects.all(),
                        'apparts': Appart.objects.filter(fonction_psl='Proviseur'),
                        'schools': School.objects.all(),
                        'personals': Personal.objects.filter(fonc_grd_psl='EN')}
        return render(request, 'administrator/all_stats_schools.html', stat_context)
    else:
        return redirect(error403)


def manageInfra(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ValidateUserForm(request.POST)
            if request.POST["class_or_inf"] == '1':
                cycle = Cycle.objects.get(id=request.POST["id_ccl"])
                school = School.objects.get(id=request.POST["id_sch"])
                letter = LetterAl.objects.get(id=request.POST["id_let"])

                infrastructure = Infrastructure.objects.create(
                    name_inf=request.POST["name_inf"],
                    state_inf=request.POST["state_inf"],
                    status_inf=request.POST["status_inf"],
                    abbrv_inf=request.POST["abbrv_inf"],
                    desc_inf=request.POST["desc_inf"],
                    img_inf=request.POST["img_inf"],
                    class_or_inf=request.POST["class_or_inf"],
                    letter=letter,
                    last_modify_inf=datetime.date.today(),
                    cycle=cycle,
                    school=school,
                    capacity=0,
                    total_boys=0,
                    total_girls=0,
                    total_tables=0,
                    total_handic=0
                )
                infrastructure.save()
            if request.POST["class_or_inf"] == '0':
                cycle = Cycle.objects.get(id=request.POST["id_ccl"])
                school = School.objects.get(id=request.POST["id_sch"])
                letter = LetterAl.objects.get(id=request.POST["id_let"])

                infrastructure = Infrastructure.objects.create(
                    name_inf=request.POST["name_inf"],
                    state_inf=request.POST["state_inf"],
                    status_inf=request.POST["status_inf"],
                    abbrv_inf=request.POST["abbrv_inf"],
                    desc_inf=request.POST["desc_inf"],
                    img_inf=request.POST["img_inf"],
                    class_or_inf=request.POST["class_or_inf"],
                    letter=letter,
                    last_modify_inf=datetime.date.today(),
                    cycle=cycle,
                    school=school,
                    capacity=request.POST["capacity"],
                    total_boys=request.POST["total_boys"],
                    total_girls=request.POST["total_girls"],
                    total_tables=request.POST["total_tables"],
                    total_handic=request.POST["total_handic"]
                )
                infrastructure.save()

            infrastructures = Infrastructure.objects.filter(school=school.id, class_or_inf='1')
            classes = Infrastructure.objects.filter(school=school.id, class_or_inf='0')
            offers = Offer.objects.filter(school=school.id)
            apparts = Appart.objects.filter(school=school.id)
            sch_context = {'title': 'GESTION INTERNE DE L\'ECOLE : ' + school.name_sch,
                           'infrastructures': infrastructures,
                           'offers': offers, 'apparts': apparts, 'classes': classes}
            return render(request, 'administrator/in_school.html', sch_context)

        apt_context = {'title': 'GESTION DES INFRASTRUCTURES (ETABLISSEMENTS - ETABLISSEMENTS)',
                       'cycles': Cycle.objects.all(),
                       'schools': School.objects.all(),
                       'letters': LetterAl.objects.all(),
                       'apparts': Appart.objects.all(),
                       }
        return render(request, 'administrator/infrastructures.html', apt_context)
    else:
        return redirect(error403)


def createPers(request):
    if request.user.is_authenticated:

        psl_context = {'title': 'GESTION DU PERSONNEL',
                       'personals': Personal.objects.all(),
                       'status': StatusPsl.objects.all(),
                       'schools': School.objects.all(),
                       'apparts': Appart.objects.all(),
                       'arrondissements': Arrondissement.objects.all(),
                       'olds': OldClass.objects.all()}
        if request.method == "POST":
            form = ValidateUserForm(request.POST)

            personal = Personal.objects.create(
                name_psl=request.POST["name_psl"],
                sec_name_psl=request.POST["sec_name_psl"],
                genre=request.POST["genre"],
                password_psl=request.POST["password_psl"],
                email_psl=request.POST["email_psl"],
                img_psl='/images/personals/' + request.POST["img_psl"],
                date_naiss=request.POST["date_naiss"],
                mat_number_psl=request.POST["mat_number_psl"],
                cat_psl=request.POST["cat_psl"],
                fonc_grd_psl=request.POST["fonc_grd_psl"],
                pl_h_dip_pro=request.POST["pl_h_dip_pro"],
                pl_h_dip_aca=request.POST["pl_h_dip_aca"],
                anciennete_svr=request.POST["anciennete_svr"],
                old=OldClass.objects.get(id=request.POST["old"]),
                status=StatusPsl.objects.get(id=request.POST["status"]),
                last_activity=datetime.date.today(),
                last_modify_pers=datetime.date.today()
            )
            if Personal.objects.get(name_psl=request.POST["name_psl"]) is None:
                personal.save()
            if Personal.fonc_grd_psl == 'EN':
                try:
                    user = User.objects.get(username=request.POST["name_psl"])
                except User.DoesNotExist:
                    user = User(username=request.POST["name_psl"], password=request.POST["password_psl"])
                    user.is_staff = True
                    user.is_superuser = False
                    user.save()

            return render(request, 'administrator/personals.html', psl_context)

        dhb_context = {'title': 'Le personnel'}
        return render(request, 'administrator/personals.html', psl_context)
    else:
        return redirect(error403)


def publicDetails(request, id_sch):
    school = School.objects.get(id=id_sch)
    infrastrutures = Infrastructure.objects.filter(school=id_sch, class_or_inf='1')
    classes = Infrastructure.objects.filter(school=id_sch, class_or_inf='0')
    apparts = Appart.objects.filter(school=id_sch)
    # Detail.objects.get(infrastruture=infrastruture.id_inf).year_dtl
    regions = Region.objects.all()
    offers = Offer.objects.filter(school=id_sch)
    schools = School.objects.all()
    arrs = Arrondissement.objects.all()
    i = -1
    wel_context = {'title': 'Détails sur l\'établissemenr', 'regions': regions, 'schools': schools, 'arrs': arrs,
                   'school': school, 'infrastrutures': infrastrutures, 'apparts': apparts, 'i': i, 'offers': offers,
                   'classes': classes}
    return render(request, 'public/public_details.html', wel_context)


def allSchoolVp(request):
    # Detail.objects.get(infrastruture=infrastruture.id_inf).year_dtl
    schools = School.objects.all()
    regions = Region.objects.all()
    arrs = Arrondissement.objects.all()
    i = -1
    wel_context = {'title': 'Détails sur l\'établissemenr', 'schools': schools, 'arrs': arrs, 'regions': regions}
    return render(request, 'public/all_school.html', wel_context)


def publicMapSchool(request, id_sch):
    # Detail.objects.get(infrastruture=infrastruture.id_inf).year_dtl
    school = School.objects.get(id=id_sch)
    schools = School.objects.all()
    regions = Region.objects.all()
    arrs = Arrondissement.objects.all()
    i = -1
    wel_context = {'title': 'Localisation géographique ', 'school': school, 'schools': schools, 'arrs': arrs,
                   'regions': regions}
    return render(request, 'public/map_school.html', wel_context)


def ChoiceSchool(request):
    schools = School.objects.all()
    regions = Region.objects.all()
    choice_context = {'title': "ORIENTATION : Choix d'une école ", 'schools': schools, regions: 'regions'}
    return render(request, 'public/choice_orientation.html', choice_context)


def Welcome(request):
    regions = Region.objects.all()
    schools = School.objects.all()
    arrs = Arrondissement.objects.all()
    wel_context = {'title': 'Accueil', 'regions': regions, 'schools': schools, 'arrs': arrs}
    return render(request, 'public/index.html', wel_context)


def statRgn(request, id_rgn):
    region = Region.objects.get(id=id_rgn)
    regions = Region.objects.all()
    departments = Department.objects.filter(region=id_rgn)
    schools = School.objects.all()
    arrondissements = Arrondissement.objects.all()
    wel_context = {'title': 'Statistiques', 'regions': regions, 'schools': schools,
                   'arrondissements': arrondissements, 'region': region, 'departments': departments}
    return render(request, 'public/statistiques_rgn.html', wel_context)


def publicRegion(request, id_rgn):
    region = Region.objects.get(id=id_rgn)
    regions = Region.objects.all()
    schools = School.objects.all()
    arrs = Arrondissement.objects.all()
    departments = Department.objects.filter(region=id_rgn)
    wel_context = {'title': 'Statistiques', 'regions': regions, 'schools': schools, 'arrs': arrs,
                   'region': region, 'departments': departments}
    return render(request, 'public/services-2.html', wel_context)


def publicSearch(request):
    regions = Region.objects.all()
    schools = School.objects.all()
    arrs = Arrondissement.objects.all()
    if request.GET["search"] is not None:
        query = request.GET["search"]
    else:
        query = request.POST["search"]
    result_object = School.objects.filter(name_sch__icontains=query)
    # result_object = result_object.append(School.objects.filter(system_sch__icontains=query))
    rst_srh_context = {'title': 'Résultats liés à : ' + query, 'result_object': result_object,
                       'regions': regions, 'schools': schools, 'arrs': arrs}
    return render(request, 'public/result_public_search.html', rst_srh_context)


def publicSearch2(request):
    regions = Region.objects.all()
    schools = School.objects.all()
    arrs = Arrondissement.objects.all()

    query = request.POST["search"]
    result_object = School.objects.filter(name_sch__icontains=query)
    # result_object = result_object.append(School.objects.filter(system_sch__icontains=query))
    rst_srh_context = {'title': 'Résultats liés à : ' + query, 'result_object': result_object,
                       'regions': regions, 'schools': schools, 'arrs': arrs}
    return render(request, 'public/result_public_search.html', rst_srh_context)
