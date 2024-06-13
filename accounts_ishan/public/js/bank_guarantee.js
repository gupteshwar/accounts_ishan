frappe.ui.form.on('Bank Guarantee', {
	refresh: function(frm) {
        if (frm.doc.docstatus == 1) {
            frappe.db.get_list('Journal Entry', {
                fields: ['name'],
                filters: {
                    "remark": frm.doc.name
                }
            }).then(records => {
                if (records.length === 0 ){
                    frm.add_custom_button('Create Journal Entry', () => {
                        frappe.db.get_value("Company", frm.doc.company, "abbr").then(r => {
                            if (r.message) {
                                const company_abbr = r.message.abbr;
                
                                frappe.run_serially([
                                    () => frappe.new_doc('Journal Entry'),
                                    () => {
                                        cur_frm.set_value('voucher_type', 'Journal Entry');
                                        cur_frm.set_value('company', frm.doc.company);
                                        cur_frm.set_value('remark', frm.doc.name);
                                        
                                        var ACCOUNTS_LIST = [
                                            {
                                                account: 'Bank Charges - ' + company_abbr,
                                                debit_in_account_currency: frm.doc.charges,
                                                credit_in_account_currency: 0
                                            },
                                            {
                                                account: 'Input Tax CGST - ' + company_abbr,
                                                debit_in_account_currency: frm.doc.charges * 0.09,
                                                credit_in_account_currency: 0
                                            },
                                            {
                                                account: 'Input Tax SGST - ' + company_abbr,
                                                debit_in_account_currency: frm.doc.charges * 0.09,
                                                credit_in_account_currency: 0
                                            },
                                            {
                                                account: frm.doc.account,
                                                debit_in_account_currency: 0,
                                                credit_in_account_currency: frm.doc.charges + (frm.doc.charges * 0.18),
                                            }
                                        ];
                
                                        cur_frm.clear_table("accounts");
                
                                        // Iterate over each account object in the array
                                        ACCOUNTS_LIST.forEach(function(accountDetails) {
                                            // Add a child record for each account
                                            cur_frm.add_child("accounts", {
                                                account: accountDetails.account,
                                                debit_in_account_currency: accountDetails.debit_in_account_currency,
                                                credit_in_account_currency: accountDetails.credit_in_account_currency,
                                            });
                                        });
                
                                        cur_frm.refresh_field("accounts");
                                    },
                                    () => {
                                        // Route to the new Journal Entry form
                                        frappe.set_route('Form', 'Journal Entry', cur_frm.doc.name);
                                    },
                                    () => {
                                        // Add a minor delay to ensure the form is loaded before saving
                                        return new Promise(resolve => {
                                            setTimeout(() => {
                                                // Save the document
                                                cur_frm.save();
                                                resolve();
                                            }, 100); // Minor delay of 500 milliseconds
                                        });
                                    }
                                ]);
                            }
                        });
                    }).addClass("btn-primary");
                }
            })
        }
    }
})