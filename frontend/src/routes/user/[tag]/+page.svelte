<script lang="ts">
    import type { PageProps } from './$types';
    import Icon from "@iconify/svelte"
    import { abbreviateContinent } from '$lib/utils/abbrContinent';
    import Review from '$lib/modules/review.svelte';

    let { data }: PageProps = $props();


    console.log(data)
</script>

<content class="w-full h-full flex flex-col space-y-4 px-2 py-2 md:py-8 overflow-hidden">
    <section class="flex flex-col px-4 md:px-0">
            <div class="flex items-center">
                <div class="w-fit flex space-x-2 items-center ">
                    <img src={`${data.rank.icon_url}`} alt={`${data.user.connect_code} main character (${data.char.character}) icon `} width="20"/>
                    <h1 class="font-bold text-lg leading-4">{data.rank.display_name.toUpperCase()}</h1>
                    <h2 class="text-lg ">{Math.round(data.rank.elo * 100) / 100}</h2>
                </div>
            </div>
            
            <div class="flex space-x-4 items-center justify-between">
                <div class="flex items-center justify-center space-x-2">
                    <img src={data.char.icon_url} alt={`${data.user.connect_code} main character (${data.char.character}) icon `} width="42"/>
                    <div class="w-fit text-start flex flex-col -space-y-2">
                        <h2 class="text-2xl ">{data.user.display_name}</h2>
                        <h1 class="font-bold text-4xl">{data.user.connect_code}</h1>
                    </div>
                </div>

                <div class="flex space-x-2">
                    <div class="flex flex-col items-center justify-center">
                        <button><Icon icon="ph:arrow-fat-up-fill" class="text-white/50" width=36/></button>
                        <p class="font-bold text-lg leading-4">13223</p>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                        <button><Icon icon="ph:arrow-fat-down-fill" class="text-red" width=36/></button>
                        
                        <p class="font-bold text-lg leading-5">123</p>
                    </div>
                </div>
            </div>
            <div class="flex space-x-3 items-center text-white/50">
                <p class="font-bold text-lg">{abbreviateContinent(data.user.ranked_profile.continent)}</p>
                <span>|</span>
                <div class="flex space-x-1 items-center justify-center"> 
                        <a href=""><Icon icon="prime:discord" width=24/></a>
                        <a href=""><Icon icon="prime:twitter" width=16/></a>
                        <a href=""><Icon icon="mdi:youtube" width=24/></a>
                        <a href=""><Icon icon="ri:bluesky-fill" width=21/></a>
                </div>
            </div>
    </section>


    <section class="w-full h-full flex flex-col overflow-hidden">
      
        <div class="relative w-full h-full bg-white/10 rounded-md overflow-y-auto overflow-x-hidden">
           <div class="flex flex-col h-full">
                {#each data.reviews.items as review}
                    <Review review={review} />
                {/each}
           </div>
            <div class="sticky bottom-2 left-0 px-2 w-full h-fit flex space-x-1 text-lg">
                <input placeholder="search ..." class="bg-gray px-4 font-bold text-white/50 rounded-md w-full border-2 border-darkgray">
                <button class="text-white/50 p-2 px-3 bg-darkgray rounded-md border-2 border-gray"><Icon icon="mdi:plus-bold" /></button>
            </div>
        </div>
    </section>

</content>