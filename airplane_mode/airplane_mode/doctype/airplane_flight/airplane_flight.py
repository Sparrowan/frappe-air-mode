# Copyright (c) 2026, Alphius Wambua and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"flights/{self.name}"

	def get_context(self, context):
		context.airline = frappe.get_value("Airplane", self.airplane, "airline") or ""

	def on_submit(self):
		self.db_set("status", "Completed")
