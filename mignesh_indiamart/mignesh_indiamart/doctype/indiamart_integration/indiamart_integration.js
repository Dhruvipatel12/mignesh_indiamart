// Copyright (c) 2023, Dhruvi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Indiamart Integration', {
	sync_lead:function(frm){

		if(!frm.doc.start_date || !frm.doc.end_date){
			frappe.throw(__("From And To Date Mandatory"))
		}
		if(frm.doc.start_date && frm.doc.end_date){
		frappe.call({
			method:"mignesh_indiamart.api.indiamart_api",
			args:{"startdate":frm.doc.start_date,"enddate":frm.doc.end_date},
			freeze:true,
			freeze_message:"Please Wait . .",
			callback:function(r){
				console.log(r)
			}
		
		})  
	    }
	}
});
