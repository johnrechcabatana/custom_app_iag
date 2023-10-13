import frappe

def insert_pi_project(self=None, Method = None):

    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_pi_list` where name =%s
        """,(name), as_dict=1)

        frappe.db.sql("""
        INSERT INTO `tabproject_pi_list`  (`name`,`purchase_invoice`,`parent`,`parentfield`,`parenttype`)VALUES(%s,%s,%s,'pi_list','Project')
        """,(name,self.name,itms.project))

def pi_project_link_delete(self=None, Method=None):
    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_pi_list` where name =%s
        """,(name), as_dict=1)