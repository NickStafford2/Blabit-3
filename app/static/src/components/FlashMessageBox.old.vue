<template>
    <div class="row justify-content-center" >
      <div class="col-6 bg-info rounded-bottom" :class="visibilityClass" id="message-box">
        <div class="float-right">
          <button :class="visibilityClass" type="button" class="close" aria-label="Close" @click="toggleShow">
            <span :class="visibilityClass" id="close-button" aria-hidden="true">&times;</span>
          </button>
        </div>
          <p :class="visibilityClass" id="message-text" v-for="message in messages" class="my-2">
            {{ message }}
          </p>
      </div>
    </div>
</template>



<script>
export default {
    props: {
        messages: {type: Array}
    },
    data() {
        return {
            //messages: ['important flash message'],
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
        hideMessageBox() {
            console.log('hide message box called')
            //this.messages=[];
            this.show=true;
        },
        showMessageBox() {
            console.log('show message box called');
            this.show = false;
        },
        handleEvent() {
            console.log('handleEvent');
        }

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
    display: inline-block;
  -webkit-transition: 1s;
  -moz-transition: 1s;
  -ms-transition: 1s;
  -o-transition: 1s;
  transition: height 1s;
  overflow: hidden;
  min-height: 0px;
}
#close-button {
    display: inline-block;
  -webkit-transition: 1s;
  -moz-transition: 1s;
  -ms-transition: 1s;
  -o-transition: 1s;
  transition: opacity 1s;
}

#message-text {
    display: inline-block;
  -webkit-transition: 1s;
  -moz-transition: 1s;
  -ms-transition: 1s;
  -o-transition: 1s;
  transition: color .5s;
}
div.hidden{
  height: 0px;
}
div.show {
  height: 75px ;
}
p.hidden{
  color: rgba(0,0,0,0);
}
p.show {
  color: black;
}
span.hidden{
  opacity: 0;
}
span.show {
  opacity: 1;
}
</style>