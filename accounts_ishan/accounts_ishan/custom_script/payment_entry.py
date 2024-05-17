import frappe

def before_save(doc, method=None):
    if not doc.mode_of_payment:
        return
    MODE_OF_PAYMENT = doc.mode_of_payment.upper()
    if MODE_OF_PAYMENT == "CHEQUE":
        doc.custom_payment_status = "In-Process"
    else:
        doc.custom_payment_status = None
