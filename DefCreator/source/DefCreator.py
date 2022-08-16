import tkinter as tk
import tkinter.ttk as ttk
import createcontent
import createfiles

TrucksEts = ["daf.2021", "daf.xf", "daf.xf_euro6", "iveco.hiway", "iveco.stralis", "man.tgx", "man.tgx_euro6", "mercedes.actros", "mercedes.actros2014", "renault.magnum", "renault.premium", "renault.t", "scania.r", "scania.r_2016", "scania.s_2016", "scania.streamline", "volvo.fh16", "volvo.fh16_2012"]
TrucksAts = ["freightliner.cascadia2019", "intnational.9900i", "intnational.lonestar", "intnational.lt", "kenworth.t680", "kenworth.w900", "mack.anthem", "peterbilt.389", "peterbilt.579", "volvo.vnl", "westernstar.49x", "westernstar.57x"]
TypeListETS = ["cup_holder", "curtain_f", "l_pillow", "set_lglass", "toyac", "toybed", "toybig", "toyhang", "toyseat", "toystand", "cordv_plate", "drv_plate", "flag_l", "flag_r", "intlight_bck", "steering_w"]
TypeListATS = ["bckpanel", "codrv_plate", "cup_holder", "drv_plate", "flag_f_l", "flag_f_r", "l_pillow", "set_lglass", "steering_w", "toyac", "toyback", "toybed", "toybig", "toyhang", "toyseat", "toystand", "toytable"]
with open("ModTrucksATS.txt") as tats:
    ModTrucksATSstr = tats.read()
ModTrucksATS = ModTrucksATSstr.split("\n")
if ModTrucksATS[0] == "":
	ModTrucksATS = []
with open("ModTrucksETS.txt") as tets:
    ModTrucksETSstr = tets.read()
ModTrucksETS = ModTrucksETSstr.split("\n")
if ModTrucksETS[0] == "":
	ModTrucksETS = []


def printwindow(message):
    windowprint = tk.Tk()
    windowprint.title("Message")
    label = tk.Label(master=windowprint, text=message)
    label.pack()


def mainscreenother(game):
    def runother():
        if game=="ATS" and use_modlist.get():
            trucklist = TrucksAts + ModTrucksATS
        elif game=="ATS" and not use_modlist.get():
            trucklist = TrucksAts
        elif not use_modlist.get():
            trucklist = TrucksEts
        else:
            trucklist = TrucksEts + ModTrucksETS

        content = text_box.get("1.0", "end")[:-1]
        filename = ent_filename.get()
        basepath = ent_path.get()
        relpath = ent_goalpath.get()

        createfiles.createdeffilesother(trucklist, content, basepath, relpath, filename)

        printwindow("successful")


    window = tk.Tk()
    window.title("DefCreator" + game + "Other")
    use_modlist = tk.BooleanVar()

    frm_easymode = tk.Frame()
    frm_advancedmode = tk.Frame()
    lbl_advanced = tk.Label(master=frm_advancedmode, text="Content:")
    text_box = tk.Text(master=frm_advancedmode)
    lbl_advanced.pack()
    text_box.pack()

    frm_checkboxes = tk.Frame()
    chb_usemodlist = tk.Checkbutton(master=frm_checkboxes, text="Use Modlist", variable=use_modlist)
    chb_usemodlist.pack()

    frm_basepath = tk.Frame(master=frm_easymode)
    lbl_path = tk.Label(master=frm_basepath, text="Path to base folder:")
    ent_path = tk.Entry(master=frm_basepath)
    lbl_goalpath = tk.Label(master=frm_basepath, text="Path in the truck folder")
    ent_goalpath = tk.Entry(master=frm_basepath)
    lbl_path.pack()
    ent_path.pack(fill=tk.X)
    lbl_goalpath.pack()
    ent_goalpath.pack(fill=tk.X)

    frm_additionalstuff = tk.Frame(master=frm_easymode)
    lbl_filename = tk.Label(master=frm_additionalstuff, text="Filename:")
    ent_filename = tk.Entry(master=frm_additionalstuff)
    lbl_filename.pack()
    ent_filename.pack()

    frm_basepath.pack(fill=tk.X)
    frm_additionalstuff.pack(fill=tk.X)

    frm_checkboxes.pack()
    frm_easymode.pack(fill=tk.X, side=tk.LEFT, expand=True)
    frm_advancedmode.pack(fill=tk.X, side=tk.LEFT, expand=True)

    frm_run = tk.Frame(master=frm_easymode)
    btn_run = tk.Button(master=frm_run, text="Create Files", command=runother)
    btn_run.pack()
    frm_run.pack(side=tk.BOTTOM)

    window.mainloop()

def mainscreen(game):
    if game == "ATS":
        TypeList = TypeListATS
    else:
        TypeList = TypeListETS

    def run():
        if game=="ATS" and use_modlist.get():
            trucklist = TrucksAts + ModTrucksATS
        elif game=="ATS" and not use_modlist.get():
            trucklist = TrucksAts
        elif not use_modlist.get():
            trucklist = TrucksEts
        else:
            trucklist = TrucksEts + ModTrucksETS

        basepath = ent_path.get()
        iconname = ent_iconname.get()

        if use_icon.get():
            createfiles.createiconfiles(basepath, iconname)

        contentadvanced = text_box.get("1.0", "end")[:-1]
        internalname = ent_internalname.get()
        filename = ent_filename.get()
        acctype = cmb_type.get()

        if use_advanced.get():
            createfiles.createdeffiles(trucklist, acctype, contentadvanced, basepath, internalname, filename)
            printwindow("successful")
            return()

        name = ent_name.get()
        price = ent_price.get()
        unlock = ent_unlock.get()

        interior = ent_intpath.get()
        interioruk = ent_intukpath.get()
        exterior = ent_expath.get()
        exterioruk = ent_exukpath.get()

        content = createcontent.createcontent(basepath, name, price, unlock, iconname, interior, exterior, interioruk, exterioruk)
        createfiles.createdeffiles(trucklist, acctype, content, basepath, internalname, filename)
        printwindow("successful")

    window = tk.Tk()
    window.title("DefCreatorAccessory" + game)
    use_modlist = tk.BooleanVar()
    use_advanced = tk.BooleanVar()
    use_icon = tk.BooleanVar()

    frm_easymode = tk.Frame()
    frm_advancedmode = tk.Frame()
    lbl_advanced = tk.Label(master=frm_advancedmode, text="Advanced Settings:")
    text_box = tk.Text(master=frm_advancedmode)
    lbl_advanced.pack()
    text_box.pack()

    frm_checkboxes = tk.Frame()
    chb_usemodlist = tk.Checkbutton(master=frm_checkboxes, text="Use Modlist", variable=use_modlist)
    chb_useadvanced = tk.Checkbutton(master=frm_checkboxes, text="Use Advanced", variable=use_advanced)
    chb_createicon = tk.Checkbutton(master=frm_checkboxes, text="Create Icon", variable=use_icon)
    chb_usemodlist.pack(side=tk.LEFT)
    chb_createicon.pack(side=tk.LEFT)
    chb_useadvanced.pack(side=tk.LEFT)

    frm_basepath = tk.Frame(master=frm_easymode)
    lbl_path = tk.Label(master=frm_basepath, text="Path to base folder:")
    ent_path = tk.Entry(master=frm_basepath)
    lbl_path.pack()
    ent_path.pack(fill=tk.X)

    frm_models = tk.Frame(master=frm_easymode)
    lbl_intpath = tk.Label(master=frm_models, text="Path to interior model:")
    ent_intpath = tk.Entry(master=frm_models)
    lbl_expath = tk.Label(master=frm_models, text="Path to exterior model (optional):")
    ent_expath = tk.Entry(master=frm_models)
    lbl_intukpath = tk.Label(master=frm_models, text="Path to interior_UK model (optional):")
    ent_intukpath = tk.Entry(master=frm_models)
    lbl_exukpath = tk.Label(master=frm_models, text="Path to exterior_UK model (optional):")
    ent_exukpath = tk.Entry(master=frm_models)
    lbl_intpath.pack()
    ent_intpath.pack(fill=tk.X)
    lbl_expath.pack()
    ent_expath.pack(fill=tk.X)
    lbl_intukpath.pack()
    ent_intukpath.pack(fill=tk.X)
    lbl_exukpath.pack()
    ent_exukpath.pack(fill=tk.X)

    frm_additionalstuff = tk.Frame(master=frm_easymode)
    lbl_iconname = tk.Label(master=frm_additionalstuff, text="Name of Icon (has to be the same as the name of your tga file):")
    ent_iconname = tk.Entry(master=frm_additionalstuff)
    lbl_internalname = tk.Label(master=frm_additionalstuff, text="Internal Name (you will never see it, has to be unique, max 12letters):")
    ent_internalname = tk.Entry(master=frm_additionalstuff)
    lbl_filename = tk.Label(master=frm_additionalstuff, text="Filename:")
    ent_filename = tk.Entry(master=frm_additionalstuff)
    lbl_iconname.pack()
    ent_iconname.pack(fill=tk.X)
    lbl_internalname.pack()
    ent_internalname.pack(fill=tk.X)
    lbl_filename.pack()
    ent_filename.pack()

    frm_data = tk.Frame(master=frm_easymode)
    lbl_name = tk.Label(master=frm_data, text="Name:")
    ent_name = tk.Entry(master=frm_data)
    lbl_price = tk.Label(master=frm_data, text="Price:")
    ent_price = tk.Entry(master=frm_data)
    lbl_unlock = tk.Label(master=frm_data, text="Unlock level:")
    ent_unlock = tk.Entry(master=frm_data)
    lbl_type = tk.Label(master=frm_data, text="Type:")
    cmb_type = ttk.Combobox(master=frm_data, values=TypeList)
    lbl_name.grid(row=0, column=0)
    lbl_price.grid(row=0, column=1)
    ent_name.grid(row=1, column=0)
    ent_price.grid(row=1, column=1)
    lbl_unlock.grid(row=2, column=0)
    lbl_type.grid(row=2, column=1)
    ent_unlock.grid(row=3, column=0)
    cmb_type.grid(row=3, column=1)

    frm_data.pack()
    frm_basepath.pack(fill=tk.X)
    frm_models.pack(fill=tk.X)
    frm_additionalstuff.pack(fill=tk.X)

    frm_checkboxes.pack()
    frm_easymode.pack(fill=tk.X, side=tk.LEFT, expand=True)
    frm_advancedmode.pack(fill=tk.X, side=tk.LEFT, expand=True)

    frm_run = tk.Frame(master=frm_easymode)
    btn_run = tk.Button(master=frm_run, text="Create Files", command=run)
    btn_run.pack()
    frm_run.pack(side=tk.BOTTOM)

    window.mainloop()

def secondscreen(game):
    def mainscreenaccprepare():
        window.destroy()
        mainscreen(game)

    def mainscreenotherprepare():
        window.destroy()
        mainscreenother(game)

    window = tk.Tk()
    window.title("DefCreator")
    lbl_game = tk.Label(text="Type:")
    lbl_game.pack()
    btn_acc = tk.Button(text="Accessoires",
                        command=mainscreenaccprepare,
                        width=25,
                        height=5,
                        bg="black",
                        fg="white",)
    btn_other = tk.Button(text="Other",
                        command=mainscreenotherprepare,
                        width=25,
                        height=5,
                        bg="black",
                        fg="white", )
    btn_acc.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    btn_other.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    window.mainloop()

def startscreen():
    def mainscreenATS():
        window.destroy()
        secondscreen("ATS")

    def mainscreenETS():
        window.destroy()
        secondscreen("ETS")

    window = tk.Tk()
    window.title("DefCreator")
    lbl_game = tk.Label(text="Game")
    lbl_game.pack()
    btn_ATS = tk.Button(text="ATS",
                        command=mainscreenATS,
                        width=25,
                        height=5,
                        bg="black",
                        fg="white",)
    btn_ETS = tk.Button(text="ETS",
                        command=mainscreenETS,
                        width=25,
                        height=5,
                        bg="black",
                        fg="white", )
    btn_ATS.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    btn_ETS.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    window.mainloop()

startscreen()
