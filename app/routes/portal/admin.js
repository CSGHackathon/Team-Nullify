import Ember from 'ember';

export default Ember.Route.extend({
  setupController: function (controller){
    controller.set('authController', this.controllerFor('auth'));
  },
});
