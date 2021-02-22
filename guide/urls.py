from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from guide.views import dashbordAdm, manageRgn, listRgn, precisionRgn, precisionDpt, precisionArr, search, inSchool, \
    inClass, addRegion, plotMap, managePers, modifPers, deleteRgn, listSch, allSchools, Welcome, statRgn, publicRegion, \
    publicDetails, allSchoolVp, publicMapSchool, createPers, deletePers, modifPersF, allStats, ChoiceSchool, error403, \
    publicSearch, manageApprt, freeSchool, updateSchool, deleteSchool, updateRegion, manageOffer, manageInfra, \
    submitStatClass, manageSession, manageCoursesClass, stautsPers, deleteStatus, updateStatus, allStatsSchools, \
    publicSearch2

urlpatterns = [
    path('auth/', include('app_auth.urls')),
    path('administration/search', search, name="search"),
    path('administration/', dashbordAdm, name="dashbordAdm"),
    path('region0', manageRgn, name="manageRgn"),
    path('region/', listRgn, name="listRgn"),
    path('region/<int:id_region>', precisionRgn, name="precisionRgn"),
    path('department/<int:id_dep>', precisionDpt, name="precisionDpt"),
    path('arrondissement/<int:id_arr>', precisionArr, name="precisionArr"),
    path('school/<int:id_sch>', inSchool, name="inSchool"),
    path('class/<int:id_cls>', inClass, name="inClass"),
    #path('aregion/>', addRegion, name="addRegion"),
    path('localisation/<int:id_sch>', plotMap, name="plotMap"),
    path('personal/', managePers, name="managePers"),
    path('supprimer/<int:id_region>', deleteRgn, name="deleteRgn"),
    path('personals/', listSch, name="listSch"),
    path('personals/<int:id_psl>', deletePers, name="deletePers"),
    path('schools/', allSchools, name="allSchools"),
    path('statistique_adm/', allStatsSchools, name="allStatsSchools"),
    path('recherche_etab/', publicSearch2, name="publicSearch2"),
    path('administration/modification/<int:id_psl>', modifPers, name="modifPers"),
    path('public/statictistiques/<int:id_rgn>', statRgn, name="statRgn"),
    path('', Welcome, name="Welcome"),
    path('accueil/', Welcome, name="Welcome"),
    path('details_region/<int:id_rgn>', publicRegion, name="publicRegion"),
    path('public_details/<int:id_sch>', publicDetails, name="publicDetails"),
    path('etablissements/', allSchoolVp, name="allSchoolVp"),
    path('mapper_ecole/<int:id_sch>', publicMapSchool, name="publicMapSchool"),
    path('ajout_pers', createPers, name='createPers'),
    path('personal0', modifPersF, name='modifPersF'),
    path('statistiques', allStats, name='allStats'),
    path('orientation', ChoiceSchool, name='ChoiceSchool'),
    path('Erreur-403', error403, name='error403'),
    path('resultats_recherche', publicSearch, name='publicSearch'),
    path('gestion_dep_etab', freeSchool, name='freeSchool'),
    path('modification_etablablissement', updateSchool, name='updateSchool'),
    path('delete_sch/<int:id_sch>', deleteSchool, name='deleteSchool'),
    path('region', updateRegion, name='updateRegion'),
    path('offres', manageOffer, name='manageOffer'),
    path('infrastructure', manageInfra, name='manageInfra'),
    path('en_classe', submitStatClass, name='submitStatClass'),
    path('sessions', manageSession, name='manageSession'),
    path('salles_classe', manageCoursesClass, name='manageCoursesClass'),
    path('status_personnels', stautsPers, name='stautsPers'),
    path('status_personnel/<int:id_stp>', updateStatus, name='updateStatus'),
    path('delete_status/<int:id_stp>', deleteStatus, name='deleteStatus'),
    path('apparteances', manageApprt, name='manageApprt')
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
