<script lang="ts">
    import logoBlack from '$lib/images/logo/logo-black.svg'
    import logoWhite from '$lib/images/logo/logo-white.svg'

    import Icon from "@iconify/svelte"
</script>


<nav class="bg-black border-b-2 border-white/10 flex w-full justify-between items-center py-4 px-6 md:px-20 sticky z-20 top-0">
    <a href="/">
        <img
            src={logoWhite}
            width={72}
            alt="Logo white"
        />
    </a>

    <div class="h-full space-x-2 flex">
        <!-- <button><Icon icon="line-md:sunny-loop" class="text-white" width=48/></button> -->
        <!-- <button><Icon icon="line-md:moon-loop" class="text-white" width=48/></button> -->
        <button><Icon icon="mdi-search" class="text-white" width=32/></button>
        <button><Icon icon="mdi-user" class="text-white" width=32/></button>
    </div>
</nav>