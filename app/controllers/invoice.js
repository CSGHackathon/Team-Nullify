import Ember from 'ember';

export default Ember.Controller.extend({
	authController: null,
	graphData:{},
	actions:{
		downloadPDF: function(){
			var pdf = new jsPDF('p', 'pt', 'letter');
			var source = Ember.$('#canvas')[0];
			var margins = {
				top: 20,
				bottom: 20,
				left: 20,
				width: 800
			};
			pdf.addHTML(
			source,
			margins.left,
			margins.top, {
				'width': margins.width,
			},

			function (dispose) {
				pdf.save('Invoice.pdf');
			}, margins);
    	},
 	}
});
