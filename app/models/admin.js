import DS from 'ember-data';

export default DS.Model.extend({
  acct_name: DS.attr('string'),
  body: DS.attr('string'),
  date: DS.attr('string'),
  phone: DS.attr('string'),
  time: DS.attr('string')
});
