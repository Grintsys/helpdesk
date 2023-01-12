import frappe


def execute():
	frappe.reload_doc("Helpdesk", "doctype", "Agent")
	frappe.reload_doc("Helpdesk", "doctype", "Agent Group Item")
	frappe.reload_doc("Helpdesk", "doctype", "Agent Group")
	frappe.reload_doc("Helpdesk", "doctype", "Helpdesk Settings")

	all_groups = frappe.get_all("Agent Group", fields=["name"])
	for group in all_groups:
		group_doc = frappe.get_doc("Agent Group", group.name)
		group_doc.create_assignment_rule()
		group_doc.save()

	agents = frappe.get_all("Agent")
	for agent in agents:
		agent_doc = frappe.get_doc("Agent", agent.name)
		agent_doc.is_active = True
		agent_doc.save()
