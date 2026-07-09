# Copyright (c) 2026, Alphius Wambua and contributors
# For license information, please see license.txt

import random

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_insert(self):
		self.seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"

	def validate(self):
		self.calculate_total_amount()
		self.remove_duplicate_addons()

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Cannot submit ticket. Ticket status must be 'Boarded' before submission.")

	def calculate_total_amount(self):
		total = self.flight_price or 0
		for addon in self.add_ons:
			total += addon.amount or 0
		self.total_amount = total

	def remove_duplicate_addons(self):
		seen = set()
		unique = []
		for addon in self.add_ons:
			if addon.item not in seen:
				seen.add(addon.item)
				unique.append(addon)
		self.add_ons = unique
