<script lang="ts">
    import type { Review } from "$lib/types/review";
    import Icon from "@iconify/svelte"

    const { review } = $props();

</script>

<article class="flex flex-col space-y-1 border-b-2 border-white/10 px-3 py-2">
    <!-- <h1>{review.created_by}</h1> -->
    <header class="flex space-x-4 items-center justify-between">
        <a href="/user/hbox-305" class="flex items-center justify-center space-x-2">
            <img src={"https://slippi.gg/images/characters/stock-icon-15-0.png"} alt={`HBOX-305 main character (JIGGLYPUFF) icon `} width=32/>
            <div class="w-fit text-start flex flex-col -space-y-2">
                <h2 class="text-lg ">Hungrybox</h2>
                <h1 class="font-bold text-xl">HBOX#305</h1>
            </div>
        </a>

        <div class="flex space-x-2">
            <div class="flex flex-col items-center justify-center">
                <button><Icon icon="ph:arrow-fat-up-fill" class="text-white/50" width=24/></button>
                <p class="font-bold text-lg leading-4">2</p>
            </div>
            <div class="flex flex-col items-center justify-center">
                <button><Icon icon="ph:arrow-fat-down-fill" class="text-red" width=24/></button>
                
                <p class="font-bold text-lg leading-5">0</p>
            </div>
        </div>
    </header>

    <content class="text-md leading-5">
        this guy is really cool tbh i kinda fucked with the way he spammed taunt all the time and...
    </content>

    <footer class="flex w-full items-center justify-between text-md text-white/50 pt-1">
        <div class="text-xl flex items-center justify-center space-x-2">
            <button><Icon icon='material-symbols:bookmark-outline'/></button>
            <button><Icon icon='bx:repost' class="text-2xl"/></button>
            <button><Icon icon='majesticons:share-line' class="text-xl"/></button>
            <button><Icon icon='ph:flag-bold' class="text-lg"/></button>
        </div>
        <button class="text-sm font-bold">READ MORE</button>
    </footer>
</article>