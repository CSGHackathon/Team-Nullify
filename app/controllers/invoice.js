import Ember from 'ember';

export default Ember.Controller.extend({
	authController: null,
	graphData:{},
	actions:{
		downloadPDF: function(){
			var pdf = new jsPDF('l', 'pt', 'a3');
			var source = Ember.$('#canvas')[0];
			var margins = {
				top: 10,
				bottom: 10,
				left: 10,
				width: 300
			};
			pdf.fromHTML(
			source,
			margins.left,
			margins.top, {
				'width': margins.width,
			},

			function (dispose) {
				pdf.save('Invoice.pdf');
			}, margins);
    	},
    	/*downloadPDF: function(){
    		getCanvas().then(function(canvas){
			var img = canvas.toDataURL("image/png"),
			doc = new jsPDF({
			      unit:'px', 
			      format:'a4'
			    });     
			    doc.addImage(img, 'JPEG', 20, 20);
			    doc.save('techumber-html-to-pdf.pdf');
			    form.width(cache_width);
			});
    	},
    	getCanvas: function(){
			form.width((a4[0]*1.33333) -80).css('max-width','none');
			return html2canvas(form,{
				imageTimeout:2000,
				removeContainer:true
			}); 
		}*/
		/*html2canvas($("#canvas"), {
            onrendered: function(canvas) {         
                var imgData = canvas.toDataURL(
                    'image/png');              
                var doc = new jsPDF('p', 'mm');
                doc.addImage(imgData, 'PNG', 10, 10);
                doc.save('sample-file.pdf');
            }
        });*/
		/*downloadPDF: function(){
			html2canvas(Ember.$('#canvas'), {
				onrendered: function(canvas){
					var myImage = canvas.toDataURL("image/png");
					window.open(myImage);
				}
			})
		}*/
 	}
});
