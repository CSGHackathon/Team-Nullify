import DS from 'ember-data';

export default DS.Model.extend({
  companyName: DS.attr('string'),
  invoiceStatement: DS.attr('string')
});
