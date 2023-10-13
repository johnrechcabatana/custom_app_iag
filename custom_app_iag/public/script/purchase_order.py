import frappe

def insert_po_project(self=None, Method = None):

    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_po_list` where name =%s
        """,(name), as_dict=1)

        frappe.db.sql("""
        INSERT INTO `tabproject_po_list`  (`name`,`purchase_order`,`parent`,`parentfield`,`parenttype`)VALUES(%s,%s,%s,'po_list','Project')
        """,(name,self.name,itms.project))

def po_project_link_delete(self=None, Method=None):
    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_po_list` where name =%s
        """,(name), as_dict=1)