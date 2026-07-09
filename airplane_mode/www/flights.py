import frappe


def get_context(context):
	context.flights = frappe.get_all(
		"Airplane Flight",
		filters={"is_published": 1},
		fields=[
			"name", "route", "airplane",
			"source_airport_code", "destination_airport_code",
			"date_of_departure", "time_of_departure", "duration",
		],
		order_by="date_of_departure asc",
	)
	for flight in context.flights:
		flight.airline = frappe.get_value("Airplane", flight.airplane, "airline") or ""
		# Use route field if set, otherwise build from name (for existing records)
		flight.detail_url = flight.route or f"flights/{flight.name}"
