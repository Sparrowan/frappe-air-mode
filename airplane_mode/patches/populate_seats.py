import random

import frappe


def execute():
	tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["in", ["", None]]}, pluck="name")
	for ticket_name in tickets:
		seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"
		frappe.db.set_value("Airplane Ticket", ticket_name, "seat", seat, update_modified=False)
