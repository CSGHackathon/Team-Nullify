import Ember from 'ember';

export default Ember.Controller.extend({
  authController: undefined,
  userName: '',
  password: '',
  rememberMe: false,
  isAdminRoute: function () {
    var currentRouteName = this.controllerFor('application').get('currentRouteName');
    if (currentRouteName === 'portal.admin' ) {
      return true;
    }
    else {
      return false;
    }
  },

  /**
  Whether or not to request name for chat

  @property displayNameForm
  @public
  @type String
  @default 'true'
  */
  displayNameForm: 'true',

  isDisplayNameForm: Ember.computed('displayNameForm', {
    get() {
      var displayNameForm = this.get('displayNameForm');
      return displayNameForm === 'true';
    }
  }),

  /**
  Get the display name for the chat window

  @property displayName
  @public
  @type String
  @default 'true'
  */
  displayName: '',

  getDisplayName: Ember.computed('displayName', {
    get() {
      return Ember.$('h3#modal-title').html().substring(8,1000).slice(0, -1);
    }
  }),

  actions: {
    submitLogin: function() {
      console.log("portal Controller");
      var userName = this.get('userName');
      var password = this.get('password');
      var rememberMe = this.get('rememberMe');
      var authController = this.get('authController');
      authController.userLogin({'userName': userName, 'password': password, 'rememberMe': rememberMe});
    },

    addMessage: function() {
      var newMessage = this.store.createRecord('portal', {
        name: Ember.$('h3#modal-title').html().substring(8,1000).slice(0, -1),
        body: Ember.$('input#msgInput').val()
      });
      newMessage.save();
      this.setProperties({
        name: '',
        body: ''
      });
    },    

    /**
    Called when Submit button is clicked on the name entry for the chat form.

    @method submitName
    @private
    */
    submitName: function() {
      this.set('displayNameForm', false);

      const loginName = Ember.$('input#entryName').val();
      Ember.$('h3#modal-title').html(`Welcome ${loginName}!`);
    },
  }
});
