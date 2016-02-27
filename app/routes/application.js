import Ember from 'ember';

export default Ember.Route.extend({
  beforeModel: function(transition){
    this.authCheck(transition);

    // Forward all request for index to portal
    //if (transition.targetName === 'index' ){
    //  this.transitionTo('portal');
    //}
  },
  authCheck: function(transition){
    //Method to check user credentials and redirect if necessary
    var t = this;
    var auth = t.controllerFor('auth');

    console.log('auth.isAuthenticated: ', auth.isAuthenticated);
    console.log('transition.targetName: ', transition.targetName);

    // If not in whitelist or authenticated send user to portal
    if (!auth.inwhiteList(transition.targetName)) {
    	if (!auth.isRemembered()) {
        if (!auth.isAuthenticated) {
          auth.set('currentTransition', transition);
          transition.abort();
          t.transitionTo('portal.index');
        }
    	}
	  }
  },
  actions: {
    willTransition: function(transition){
      this.authCheck(transition);
    }
  }
});