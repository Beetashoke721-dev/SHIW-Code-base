# Copyright (c) 2025, beetashoke chakraborty and contributors
# For license information, please see license.txt

import frappe


@frappe.whitelist()
def get_all_uom_settings():
    """Get all Number Card UOM settings as a dictionary"""
    settings = frappe.get_all(
        "Number Card UOM Setting",
        fields=["number_card", "uom"]
    )
    return {s.number_card: s.uom for s in settings}

