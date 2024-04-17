import frappe

def before_save(doc,method=None):
    if doc.is_return and not doc.return_against:
        frappe.throw('Please create a sales invoice before creating a credit note')