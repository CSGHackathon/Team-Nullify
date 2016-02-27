import Ember from 'ember';

export default Ember.Controller.extend({

  companyName: null,
  invoiceStatement: null,

  actions: {
    updateDB: function() {
    	var cName = this.get("companyName");
    	var iState = this.get("invoiceStatement");
    	this.store.createRecord('editinvoice', {
    		companyName: cName,
    		invoiceStatement: iState,
    	});
    },
	},
});
