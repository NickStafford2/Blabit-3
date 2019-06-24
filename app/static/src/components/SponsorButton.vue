<template>
	<button type="button" :class="css" class="btn blab-button" @click="click">{{message}}</button>
</template>


<script>
	export default {
		props: {
			am_i_sponsor: {required: true}
		},
		data() {
			return {
				is_sponsor: 0
			}
		},
		computed: {
			message() {
				if (this.is_sponsor == 0) return 'Sponsor';
				else return 'Sponsoring';
			},
			css() {
				if (this.is_sponsor == 0) return 'btn-outline-success';
				else return 'btn-success';
			}
		},
		methods: {
			click() {
				if (this.is_sponsor == 0) {
					this.is_sponsor = 1;
					this.$emit('flash-message', 'you are now a sponsor');
				} 
				
				else {
					this.is_sponsor = 0;

					this.$emit('flash-message', 'you are no longer a sponsor');
				}
			}
		},
		created() {
			this.is_sponsor = this.am_i_sponsor;
		}
	};
</script>




<style scoped>
	.blab-button {
		width: 100px;
	}

</style>
