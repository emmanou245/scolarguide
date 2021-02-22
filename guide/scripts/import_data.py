from guide.models import Region


def run():
    for i in range(5, 15):
        region = Region()
        region.name_rgn = "Région N° #%d" % i
        region.desc_rgn = "Description N° " % i
        region.img_region = "http://default"
        region.save()
    print("Opération réussie.")
