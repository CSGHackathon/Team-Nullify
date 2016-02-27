import Ember from 'ember';

export default Ember.Controller.extend({
  model: {},
  authController: undefined,
  userName: '',
  password: '',
  rememberMe: false,

  actions: {
    submitLogin: function() {
      console.log("admin Controller");
      var userName = this.get('userName');
      var password = this.get('password');
      var rememberMe = this.get('rememberMe');
      var authController = this.get('authController');
      authController.adminLogin({'userName': userName, 'password': password, 'rememberMe': rememberMe});
    },
  }
});