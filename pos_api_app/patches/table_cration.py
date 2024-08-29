# sync_tables_patch.py in your_custom_app/patches
import frappe

def execute():
    # Check if the Insights app is installed
    if "insights" in frappe.get_installed_apps():
        try:
            # Call the method
            doc = frappe.get_doc("Insights Data Source", "Site DB")
            doc.enqueue_sync_tables()
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Error while calling enqueue_sync_tables")
