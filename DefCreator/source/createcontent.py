import os.path


def createcontent(basepath, name, price, unlock, icon, interior_model, exterior_model, interior_model_uk, exterior_model_uk):
    exmodel = ''
    intmodeluk = ''
    exmodeluk = ''
    intmodel = interior_model.replace(basepath, '').split('.')[0]
    if exterior_model:
        exmodel = '\texterior_model: "' + exterior_model.replace(basepath, '').split('.')[0] + '.pmd"\n'
    if interior_model_uk:
        intmodeluk = '\tinterior_model_uk: "' + interior_model_uk.replace(basepath, '').split('.')[0] + '.pmd"\n'
    if exterior_model_uk:
        exmodeluk = '\texterior_model_uk: "' + exterior_model_uk.replace(basepath, '').split('.')[0] + '.pmd"\n'

    return '{\n\tname: "' + name + '"\n\tprice: ' + price + '\n\tunlock: ' + unlock + '\n\ticon: "' + icon + '"\n\tpart_type: aftermarket\n\n\tinterior_model: "' + intmodel + '.pmd"\n' + exmodel + intmodeluk + exmodeluk + '}'
