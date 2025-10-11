<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
 	import Nav from '$lib/components/nav.svelte';
  import Footer from '$lib/components/footer.svelte';
	
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<main class="h-full w-full flex flex-col justify-between items-center">
	<Nav />

	<div class="flex max-w-md lg:max-w-lg h-full mx-auto justify-center text-white font-sans leading-4 overflow-hidden">
		{@render children?.()}
	</div>

	<Footer />
</main>