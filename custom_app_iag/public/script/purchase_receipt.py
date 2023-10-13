import frappe

def insert_pr_project(self=None, Method = None):

    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_pr_list` where name =%s
        """,(name), as_dict=1)

        frappe.db.sql("""
        INSERT INTO `tabproject_pr_list`  (`name`,`purchase_receipt`,`parent`,`parentfield`,`parenttype`)VALUES(%s,%s,%s,'pr_list','Project')
        """,(name,self.name,itms.project))

def pr_project_link_delete(self=None, Method=None):
    for itms in self.items: 
        name = self.name+itms.project
        frappe.db.sql("""
        DELETE FROM `tabproject_pr_list` where name =%s
        """,(name), as_dict=1)