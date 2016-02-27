import Ember from 'ember';
import config from '../config/environment';
import Mirage from 'ember-cli-mirage';
import { faker } from 'ember-cli-mirage';

export default function() {
  
  this.get('users');
  this.get('editinvoices');
}