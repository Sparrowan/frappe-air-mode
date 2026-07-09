import frappe


def get_context(context):
	if frappe.form_dict.get("flight"):
		context.web_form_doc.flight = frappe.form_dict.get("flight")
	if frappe.form_dict.get("flight_price"):
		context.web_form_doc.flight_price = frappe.form_dict.get("flight_price")
