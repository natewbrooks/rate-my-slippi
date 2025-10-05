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

	<div class="flex max-w-3xl h-full mx-auto justify-center">
		{@render children?.()}
	</div>

	<Footer />
</main>