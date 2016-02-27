import Ember from 'ember';

export default Ember.Controller.extend({
  isAdmin: false,
  isAuthenticated: false,
  remember: false,
  currentTransition: null,
  whiteList: ['portal.admin','portal.index'],
  user: {},
  inwhiteList: function(string){
    if ( this.get('whiteList').indexOf(string)>=0 ) {
      return true;
    }
    else {
      return false;
    }
  },
  isRemembered: function(){
    if (localStorage.getItem("isAuthenticated") === 'true') {
      this.set('isAuthenticated', true);
    }

    return this.get('isAuthenticated');
  },
  userLogin: function(credentials){
    var t = this;
    var currentTransition = t.get('currentTransition');

    console.log("credentials: ", credentials);

    // Server will return somthing like this
    var user = {
        name: 'Adam',
        email: 'Adam@gmail.com',
        phone_number: 4023332227,
        icon: 'user here'
      };
      t.set('user', user);

      // Set is authenticated to true
      t.set('isAuthenticated', true);

      // If the the user was redirected to authenticate send them to the page they originally requested
      if(currentTransition){
        t.set('currentTransition', null);
        currentTransition.retry();
      }

      // If the user clicked the remember me check box set is auth in local storage
      if (credentials.rememberMe === true) {
        localStorage.setItem("isAuthenticated", true); 
      }
        
  },
  adminLogin: function(credentials){
   var t = this;
   var currentTransition = t.get('currentTransition');

    console.log("credentials: ", credentials);

    // Server will return somthing like this
    var user = {
        name: 'Adam',
        email: 'Adam@gmail.com',
        phone_number: 4023332227,
        icon: 'user here'
      };
      t.set('user', user);

      // Set is authenticated to true
      t.set('isAuthenticated', true);

      // Set is authenticated to true
      t.set('isAdmin', true);

      // If the the user was redirected to authenticate send them to the page they originally requested
      if(currentTransition){
        t.set('currentTransition', null);
      }

      // If the user clicked the remember me check box set is auth in local storage
      if (credentials.rememberMe === true) {
        localStorage.setItem("isAuthenticated", true); 
      }
        
  },
  logout: function(){
    // Do the deauthentication stuff here
    this.set('user', {});
    this.set('isAuthenticated', false);
    localStorage.removeItem('isAuthenticated');

    // Redirect to the home page
    this.transitionToRoute('application');
  },
});