import frappe
from frappe import _, msgprint
from frappe.model.document import Document
from frappe.query_builder.custom import ConstantColumn
from frappe.utils import flt, fmt_money, getdate
from pypika import Order
from erpnext.accounts.doctype.bank_clearance.bank_clearance import BankClearance
import erpnext

form_grid_templates = {"journal_entries": "templates/form_grid/bank_reconciliation_grid.html"}

class CustomBankClearance(BankClearance):
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        from erpnext.accounts.doctype.bank_clearance_detail.bank_clearance_detail import (
            BankClearanceDetail,
        )

        account: DF.Link
        account_currency: DF.Link | None
        bank_account: DF.Link | None
        from_date: DF.Date
        include_pos_transactions: DF.Check
        include_reconciled_entries: DF.Check
        payment_entries: DF.Table[BankClearanceDetail]
        to_date: DF.Date
    # end: auto-generated types
    @frappe.whitelist()
    def get_payment_entries(self):
        if not (self.from_date and self.to_date):
            frappe.throw(_("From Date and To Date are Mandatory"))

        if not self.account:
            frappe.throw(_("Account is mandatory to get payment entries"))

        entries = []

        # get entries from all the apps
        for method_name in frappe.get_hooks("get_payment_entries_for_bank_clearance"):
            entries += (
                frappe.get_attr(method_name)(
                    self.from_date,
                    self.to_date,
                    self.account,
                    self.bank_account,
                    self.include_reconciled_entries,
                    self.include_pos_transactions,
                )
                or []
            )

        entries = sorted(
            entries,
            key=lambda k: getdate(k["posting_date"]),
        )

        self.set("payment_entries", [])
        default_currency = erpnext.get_default_currency()

        for d in entries:
            row = self.append("payment_entries", {})

            amount = flt(d.get("debit", 0)) - flt(d.get("credit", 0))

            if not d.get("account_currency"):
                d.account_currency = default_currency

            formatted_amount = fmt_money(abs(amount), 2, d.account_currency)
            d.amount = formatted_amount + " " + (_("Dr") if amount > 0 else _("Cr"))
            d.posting_date = getdate(d.posting_date)

            d.pop("credit")
            d.pop("debit")
            d.pop("account_currency")
            row.update(d)

    @frappe.whitelist()
    def update_clearance_date(self):
        clearance_date_updated = False
        for d in self.get("payment_entries"):
            if d.clearance_date:
                if not d.payment_document:
                    frappe.throw(_("Row #{0}: Payment document is required to complete the transaction"))

                if d.cheque_date and getdate(d.clearance_date) < getdate(d.cheque_date):
                    frappe.throw(
                        _("Row #{0}: Clearance date {1} cannot be before Cheque Date {2}").format(
                            d.idx, d.clearance_date, d.cheque_date
                        )
                    )

            if d.clearance_date or self.include_reconciled_entries:
                if not d.clearance_date:
                    d.clearance_date = None
                        
                payment_entry = frappe.get_doc(d.payment_document, d.payment_entry)
                payment_entry.db_set("clearance_date", d.clearance_date)
                payment_entry.db_set("custom_payment_status", 'Cleared')

                clearance_date_updated = True

        if clearance_date_updated:
            self.get_payment_entries()
            msgprint(_("Clearance Date updated"))
        else:
            msgprint(_("Clearance Date not mentioned"))