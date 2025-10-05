<script lang="ts">
    import logoBlack from '$lib/images/logo/logo-black.svg'
    import logoWhite from '$lib/images/logo/logo-white.svg'

    import Icon from "@iconify/svelte"
</script>


<nav class="bg-black border-b-1 border-white/10 flex w-full justify-between items-center p-8 sticky z-20 top-0">
    <img
        src={logoWhite}
        width={180}
        alt="Logo white"
    />
    Rate My Slippi

    <div class="h-full space-x-4 flex">
        <button><Icon icon="mdi-user" class="text-white" width=52/></button>
        <button><Icon icon="line-md:sunny-loop" class="text-white" width=52/></button>
        <button><Icon icon="line-md:moon-loop" class="text-white" width=42/></button>
    </div>
</nav>