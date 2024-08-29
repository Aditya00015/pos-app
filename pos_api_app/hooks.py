app_name = "pos_api_app"
app_title = "POS API App"
app_publisher = "Rajvi"
app_description = "It post the data to master site"
app_email = "rajvi@sanskartechnolab.ccom"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pos_api_app/css/pos_api_app.css"
# app_include_js = "/assets/pos_api_app/js/pos_api_app.js"
app_include_css = "/assets/pos_api_app/css/point-of-sale.css"

# include js, css files in header of web template
# web_include_css = "/assets/pos_api_app/css/pos_api_app.css"
# web_include_js = "/assets/pos_api_app/js/pos_api_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pos_api_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "pos_api_app/public/icons.svg"
# app_include_js = "/assets/pos_api_app/js/pos_item_cart_2.js"

# Home Pages
# ----------
# page_js = {"point-of-sale" : "public/js/pos_item_cart.js"}
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
# 	"methods": "pos_api_app.utils.jinja_methods",
# 	"filters": "pos_api_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pos_api_app.install.before_install"
after_install = "pos_api_app.pos_api_app.api.api.after_install"
# after_install = "pos_api_app.pos_api_app.api.api.create_or_update_database"

# fixtures = [{"dt": "User", "filters": [
#                 [
#                     "email", "in", [
#                         "franchise_user@jibu.com"
#                     ]
#                 ]
#             ]},
#             {"dt": "Role", "filters": [
#                 [
#                     "name", "in", [
#                         "Franchise Data API role"
#                     ]
#                 ]
#             ]},
#             {"dt": "Custom DocPerm", "filters": [
#                 [
#                     "Role", "in", [
#                         "Franchise Data API role"
#                     ]
#                 ]
#             ]}
#             ]

# Uninstallation
# ------------

# before_uninstall = "pos_api_app.uninstall.before_uninstall"
# after_uninstall = "pos_api_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pos_api_app.utils.before_app_install"
# after_app_install = "pos_api_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pos_api_app.utils.before_app_uninstall"
# after_app_uninstall = "pos_api_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pos_api_app.notifications.get_notification_config"

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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	"Insights Settings": "pos_api_app.pos_api_app.overrides.insights_settings.CustomInsightsSettings"
}
# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pos_api_app.tasks.all"
# 	],
# 	"daily": [
# 		"pos_api_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"pos_api_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pos_api_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pos_api_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "pos_api_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pos_api_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pos_api_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pos_api_app.utils.before_request"]
# after_request = ["pos_api_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["pos_api_app.utils.before_job"]
# after_job = ["pos_api_app.utils.after_job"]

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
# 	"pos_api_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

