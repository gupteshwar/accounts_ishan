import frappe

def before_submit(doc, method=None):
    MODE_OF_PAYMENT = doc.mode_of_payment.upper()
    if MODE_OF_PAYMENT == "CHEQUE":
        doc.custom_payment_status = "Inprocess"

def before_update_after_submit(doc, method=None):
    if doc.clearance_date:
        frappe.throw('heloo pE')