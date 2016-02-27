import Ember from 'ember';

export default Ember.Controller.extend({
  authController: undefined,
  userName: '',
  password: '',
  rememberMe: false,
  isAdminRoute: function () {
    var currentRouteName = this.controllerFor('application').get('currentRouteName');
    if (currentRouteName == 'portal.admin' ) {
      return true;
    }
    else {
      return false;
    }
  },
  actions: {
    submitLogin: function() {
      console.log("portal Controller");
      console.log();
      var userName = this.get('userName');
      var password = this.get('password');
      var rememberMe = this.get('rememberMe');
      var authController = this.get('authController');
      authController.userLogin({'userName': userName, 'password': password, 'rememberMe': rememberMe});
    },
  }
});
