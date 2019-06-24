window.axios = require('axios');
//console.log(csrf_token);
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
if (csrf_token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = csrf_token;
    console.log('axios setup finished');
} else {
    console.error('CSRF token not found');
}

import Vue from 'vue';
import App from './App.vue';
import Chat from './components/Chat.vue';
import SponsorButton from './components/SponsorButton.vue';
import SubscribeButton from './components/SubscribeButton.vue';
import FlashMessageBox from './components/FlashMessageBox.vue';

new Vue({
  el: '#app',
  components: {
    'test': App,
    'chat': Chat,
    'sponsor-button': SponsorButton,
    'subscribe-button': SubscribeButton,
    'flash-message-box': FlashMessageBox,
  }
});

/*window.Vue = require('vue');

Vue.component('test', require('./App.vue'));

const app = new Vue({
    el: '#app'
});
*/