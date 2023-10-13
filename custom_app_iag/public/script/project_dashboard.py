from frappe import _


def get_data(data=None):
	return {
		"heatmap": True,
		"heatmap_message": _("This is based on the Time Sheets created against this project"),
		"fieldname": "project",
        "internal_links": {
            "Purchase Order": ["po_list", "purchase_order"],
            "Purchase Invoice": ["pi_list", "purchase_invoice"],
            "Purchase Receipt": ["pr_list", "purchase_receipt"]
        },
		"transactions": [
			{
				"label": _("Project"),
				"items": ["Task", "Timesheet", "Issue", "Project Update"],
			},
			{"label": _("Material"), "items": ["Material Request", "BOM", "Stock Entry"]},
			{"label": _("Sales"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
			{"label": _("Purchase"), "items": ["Purchase Order","Purchase Receipt","Purchase Invoice"]},
		],
	}
