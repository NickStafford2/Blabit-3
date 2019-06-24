<template>
    <div class="chat-wrapper">
    	<h1>{{ title }}</h1>
		<p>id: {{ id }}</p>
		<p>{{ description }}</p>
		<p>is live: {{ is_live }}</p>

	</div>
</template>



<script>
	export default {
  		name: 'chat',
		props: {
			'description':        { type: String,  required: false, default: ''},
			'id':    		      { type: Number,  required: true},
			'is_live':  	      { type: Number,  required: true},
			'show_owner_options': { type: Boolean, required: true},
			'title': 		      { type: String,  required: true},
			'user_id':  	      { type: String,  required: true},
		}, 

		updated() {
			console.log('chat mounted');
		},
	};

</script>




<style>
.chat-wrapper {
	background-color: WhiteSmoke;
}
</style>