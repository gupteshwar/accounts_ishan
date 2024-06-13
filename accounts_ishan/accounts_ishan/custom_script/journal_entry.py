import frappe

def on_cancel(self, method):
    if self.voucher_type=="EMD Entry":
        doc = frappe.get_doc("EMD", {'reference_num': self.cheque_no})
        if doc.return_journal_entry or doc.return_forfeited_entry:
            frappe.db.set_value("EMD", {'reference_num': self.cheque_no}, 'journal_entry', None)

def on_submit(self, method):
        if frappe.db.exists("Bank Guarantee", self.remark, cache=True):
            frappe.db.set_value('Bank Guarantee', self.remark, 'custom_journal_entry', self.name)