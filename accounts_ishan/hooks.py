app_name = "accounts_ishan"
app_title = "Accounts Ishan"
app_publisher = "New Indictrans Technologies Pvt. Ltd."
app_description = "Accounts Development"
app_email = "info@indictrans.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accounts_ishan/css/accounts_ishan.css"
# app_include_js = "/assets/accounts_ishan/js/accounts_ishan.js"

# include js, css files in header of web template
# web_include_css = "/assets/accounts_ishan/css/accounts_ishan.css"
# web_include_js = "/assets/accounts_ishan/js/accounts_ishan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "accounts_ishan/public/scss/website"
# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Journal Entry": "public/js/journal_entry.js",
    "Bank Guarantee": "public/js/bank_guarantee.js",
    "Payment Entry": "public/js/payment_entry.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_list_js = {
    "Fixed Deposit" : "accounts_ishan/accounts_ishan/doctype/fixed_deposit/fixed_deposit_list.js",
    "EMD" : "accounts_ishan/accounts_ishan/doctype/emd/emd_list.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "accounts_ishan/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "accounts_ishan.utils.jinja_methods",
# 	"filters": "accounts_ishan.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "accounts_ishan.install.before_install"
# after_install = "accounts_ishan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "accounts_ishan.uninstall.before_uninstall"
# after_uninstall = "accounts_ishan.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "accounts_ishan.utils.before_app_install"
# after_app_install = "accounts_ishan.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "accounts_ishan.utils.before_app_uninstall"
# after_app_uninstall = "accounts_ishan.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accounts_ishan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	#"ToDo": "custom_app.overrides.CustomToDo"
	"Bank Clearance": "accounts_ishan.accounts_ishan.custom_script.overrides.bank_clearance.CustomBankClearance"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Supplier": {
        "before_save" : "accounts_ishan.accounts_ishan.custom_script.supplier.before_save",
	},
    # "Purchase Order": {
    #     "before_save" : "accounts_ishan.accounts_ishan.custom_script.purchase_order.before_save",
	# },
	# "Purchase Invoice": {
    #     "before_save" : "accounts_ishan.accounts_ishan.custom_script.purchase_invoice.before_save",
	# },
    "Sales Invoice": {
        "before_save" : "accounts_ishan.accounts_ishan.custom_script.sales_invoice.before_save",
	},
	"Payment Entry": {
        "before_save" : "accounts_ishan.accounts_ishan.custom_script.payment_entry.before_save",
	},
	"Bank Account": {
        "before_save" : "accounts_ishan.accounts_ishan.custom_script.bank_account.before_save",
	},
    "Journal Entry": {
    	"on_cancel": "accounts_ishan.accounts_ishan.doctype.journal_entry.on_cancel",
        "on_cancel": "accounts_ishan.accounts_ishan.custom_script.journal_entry.on_cancel",
        "on_submit": "accounts_ishan.accounts_ishan.custom_script.journal_entry.on_submit"
    },
    "EMD": {
		"validate":"accounts_ishan.accounts_ishan.doctype.emd.emd.validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accounts_ishan.tasks.all"
# 	],
# 	"daily": [
# 		"accounts_ishan.tasks.daily"
# 	],
# 	"hourly": [
# 		"accounts_ishan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accounts_ishan.tasks.weekly"
# 	],
# 	"monthly": [
# 		"accounts_ishan.tasks.monthly"
# 	],
# }
scheduler_events = {
	"weekly": [
		"accounts_ishan.accounts_ishan.doctype.emd.emd.send_emails"
	],
	"daily": [
		"accounts_ishan.accounts_ishan.doctype.emd.emd.change_status_on_due"
	]
}

# Testing
# -------

# before_tests = "accounts_ishan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accounts_ishan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "accounts_ishan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["accounts_ishan.utils.before_request"]
# after_request = ["accounts_ishan.utils.after_request"]

# Job Events
# ----------
# before_job = ["accounts_ishan.utils.before_job"]
# after_job = ["accounts_ishan.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"accounts_ishan.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

