<template>
  <transition 
    name="flash-message-slide"
    @enter="enter"
    @after-enter="afterEnter"
    @leave="leave"
  >

  >
    <div v-if="show" class="row justify-content-center" id="message-box" >
      <div class="col-6 bg-info rounded-bottom" >
         <div class="float-right">
          <button type="button" class="close" aria-label="Close" @click="toggleShow">
            <span id="close-button" aria-hidden="true">&times;</span>
          </button>
        </div>
       Todo
      </div>
    </div>
  </transition>
</template>



<script>
export default {
  data() {
      return {
          show: true
      }
  },
	updated() {
		console.log('flash update');
	},     
    methods: {
        toggleShow() {
            this.show = !this.show;
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



<style scoped>

#message-box {
   /* display: inline-block;*/
  overflow: hidden;
  /*transform-origin:top;*/
  /*height: 100px;*/
  /*min-height: 0px;*/
}

.flash-message-slide-enter,
.flash-message-slide-leave-to {
  /*opacity: 0;*/
  /*transform: rotateY(50deg);*/
  height: 0px;
  /*transform: scaleY(0);*/
}
/*.flash-message-slide-enter-to,
.flash-message-slide-leave {*/
  /*opacity: 1;*/
  /*transform: scaleY(1);*/
  /*transform: rotateY(0deg);
  height: 100px;*/
  /*transform: matrix(1,0,0,1,0,100px)
}*/
.flash-message-slide-enter-active,
.flash-message-slide-leave-active {
  /*transition: opacity, transform 1s ease;*/
  /*transition: transform 1s ease;*/
  transition: height 1s ease-in-out;
  overflow: hidden;
}


</style>