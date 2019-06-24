<template>
	<button type="button" :class="css" class="btn blab-button" @click="click">{{message}}</button>
</template>



<script>
	export default {
		props: {
			am_i_subscribed: {required: true}
		},
		data() {
			return {
				is_subscribed: 0
			}
		},
		computed: {
			message() {
				if (this.is_subscribed == 0) return 'Subscribe';
				else return 'Subscribed';
			},
			css() {
				if (this.is_subscribed == 0) return 'btn-outline-info';
				else return 'btn-info';
			}
		},
		methods: {
			click() {
				if (this.is_subscribed == 0) {
					this.is_subscribed = 1;
				} 
				
				else {
					this.is_subscribed = 0;	
				} 
			}
		},
		created() {
			this.is_subscribed = this.am_i_subscribed;
		}
	};
</script>




<style>
	.blab-button {
		width: 100px;

	}

</style>
