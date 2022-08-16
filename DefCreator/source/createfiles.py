import os


def createdeffilesother(Trucks, Content, Basepath, Relpath, Filename):
    contentsplit = Content.split('VEHICLE_UNIT_NAME')
    Relpathsplit = os.path.normpath(Relpath).split(os.sep)

    dir = os.path.join(Basepath, 'def')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(dir, 'vehicle')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(dir, 'truck')
    if not os.path.exists(dir):
        os.mkdir(dir)

    for i in range(len(Trucks)):
        truck = Trucks[i]
        truckContent = contentsplit[0] + truck + contentsplit[1]
        truckdir = os.path.join(dir, truck)
        if not os.path.exists(truckdir):
            os.mkdir(truckdir)
        for j in range(len(Relpathsplit)):
            truckdir = truckdir + '/' + Relpathsplit[j]
            if not os.path.exists(truckdir):
                os.mkdir(truckdir)
        with open(truckdir + '/' + Filename.split('.')[0] + '.sii', 'w') as file:
            file.write(truckContent)


def createdeffiles(Trucks, Type, Content, Basepath, InternalName, Filename):
    dir = os.path.join(Basepath, 'def')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(dir, 'vehicle')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(dir, 'truck')
    if not os.path.exists(dir):
        os.mkdir(dir)

    for i in range(len(Trucks)):
        truck = Trucks[i]
        truckContent = 'SiiNunit\n{\naccessory_addon_data : ' + InternalName + '.' + truck + '.' + Type + '\n'
        truckdir = os.path.join(dir, truck)
        if not os.path.exists(truckdir):
            os.mkdir(truckdir)
        truckdir = os.path.join(truckdir, 'accessory')
        if not os.path.exists(truckdir):
            os.mkdir(truckdir)
        truckdir = os.path.join(truckdir, Type)
        if not os.path.exists(truckdir):
            os.mkdir(truckdir)
        with open(truckdir + '/' + Filename.split('.')[0] + '.sii', 'w') as file:
            file.write(truckContent + Content + '\n}\n')


def createiconfiles(Basepath, IconName):
    path = Basepath + '/material/ui/accessory/'
    with open(path + IconName + '.mat', 'w') as filemat:
        filemat.write('material : "ui"\n{\n\ttexture : "' + IconName + '.tobj"\n\ttexture_name : "texture"\n}\n')
    with open(path + IconName + '.tobj', 'w') as filetobj:
        filetobj.write('map 2d\t' + IconName + '.tga\naddr\tclamp_to_edge clamp_to_edge\nusage ui\n')
