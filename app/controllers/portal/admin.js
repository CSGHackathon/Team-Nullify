import Ember from 'ember';

export default Ember.Controller.extend({
  model: {},
  authController: undefined,
  userName: '',
  password: '',
  rememberMe: false,

  modelArray: Ember.computed('model', {
    get () {
      const model = this.get('model');
      // const objects = model.content.content._data;


      console.log('model yo: ', model);

    }
  }),

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