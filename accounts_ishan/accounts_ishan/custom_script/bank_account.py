import frappe

def before_save(doc, method=None):
    if not doc.bank_account_no:
        return
    bank_lengths = {
        "AXIS BANK": 15,
        "ICICI BANK": 12,
        "YES BANK": 15,
        "HDFC BANK": 14
    }
    
    bank = doc.bank.upper()
    account_length = len(doc.bank_account_no)
    
    if bank in bank_lengths and account_length != bank_lengths[bank]:
        frappe.throw(f'Bank account for {bank} must be {bank_lengths[bank]} digits long')