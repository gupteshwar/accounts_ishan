import frappe

def before_save(doc,method=None):
    if not doc.pan:
        return
    PAN_4TH_LETTER = doc.pan[3]
    if PAN_4TH_LETTER == "C":
        doc.custom_supplier_category = "Corporate"
    elif PAN_4TH_LETTER == "P":
        doc.custom_supplier_category ="Noncorporate"
    elif PAN_4TH_LETTER == "F":
        doc.custom_supplier_category = "Corporate"
    elif PAN_4TH_LETTER == "H":
        doc.custom_supplier_category = "Noncorporate"