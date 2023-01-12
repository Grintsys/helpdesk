# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HelpdeskNotification(Document):
	def after_insert(self):
		frappe.publish_realtime("helpdesk:new_notification", user=self.to_user)
