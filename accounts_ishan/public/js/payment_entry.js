frappe.ui.form.on('Payment Entry', {
    refresh: function (frm){
        if (frm.doc.custom_only_outstanding == 1){
            frm.set_query("reference_name" ,"references", function (doc, cdt, cdn){
                let row = locals[cdt][cdn]
                return {
                    filters: [
                        [row.reference_doctype, 'docstatus', '=', 1],
                        [row.reference_doctype, 'company', '=', frm.doc.company],
                        [row.reference_doctype, 'customer', '=', frm.doc.party_name],
                        [row.reference_doctype, 'outstanding_amount', '>', 0]
                    ]
                };
            })
        }
    },

    custom_only_outstanding: function (frm){
        
        if (frm.doc.custom_only_outstanding == 1){
            console.log("Running")
            frm.set_query("reference_name" ,"references", function (doc, cdt, cdn){
                let row = locals[cdt][cdn]
                return {
                    filters: [
                        [row.reference_doctype, 'docstatus', '=', 1],
                        [row.reference_doctype, 'company', '=', frm.doc.company],
                        [row.reference_doctype, 'customer', '=', frm.doc.party_name],
                        [row.reference_doctype, 'outstanding_amount', '>', 0]
                    ]
                };
            })
        }
        else {
            frm.set_query("reference_name" ,"references", function (doc, cdt, cdn){
                let row = locals[cdt][cdn]
                return {
                    filters: [
                        [row.reference_doctype, 'docstatus', '=', 1],
                        [row.reference_doctype, 'company', '=', frm.doc.company],
                        [row.reference_doctype, 'customer', '=', frm.doc.party_name],
                    ]
                };
            })
        }
    }
})