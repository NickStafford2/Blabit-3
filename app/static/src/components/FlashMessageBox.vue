<template>
        <transition-expand>
          <div v-if="expanded" class="row justify-content-center" >
            <div class="col-6 bg-info rounded-bottom" id="message-box">
              <div class="float-right">
                <button type="button" class="close" aria-label="Close" @click="toggleShow">
                  <span id="close-button" aria-hidden="true">&times;</span>
                </button>
              </div>
                <p id="message-text" v-for="message in messages" class="my-2">
                  {{ message }}
                </p>
            </div>
          </div>
        </transition-expand>

</template>



<script>
import TransitionExpand from './TransitionExpand.vue';

export default {
  data() {
      return {
          expanded: true,
          messages: ['important flash message'],
      }
  },
  components: {
    TransitionExpand,
  },
	updated() {
		console.log('flash update');
	},     
    methods: {
        toggleShow() {
            this.expanded = !this.expanded;
        },
        handleEvent() {
            console.log('handleEvent');
        },
        enter(element) {
          const width = getComputedStyle(element).width;

          element.style.width = width;
          element.style.position = 'absolute';
          element.style.visibility = 'hidden';
          element.style.height = 'auto';

          const height = getComputedStyle(element).height;

          element.style.width = null;
          element.style.position = null;
          element.style.visibility = null;
          element.style.height = 0;

          // Trigger the animation.
          // We use `setTimeout` because we need
          // to make sure the browser has finished
          // painting after setting the `height`
          // to `0` in the line above.
          setTimeout(() => {
            element.style.height = height;
          });
        },

    },  
    
    computed: {
        visibilityClass: function () {
            if (this.show) {
                return 'show'
            }
            else {
                return 'hidden'
            }
        }
    }
};


</script>



<style>
.expand-enter-active,
.expand-leave-active {
  transition-property: opacity, height;
}
.expand-enter,
.expand-leave-to {
  opacity: 0;
}
</style>