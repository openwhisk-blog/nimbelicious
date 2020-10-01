<script>
  export let api;
  import Login from './Login.svelte'
  import Cloud from './Cloud.svelte'
  import Tag from './Tag.svelte'
  import { token, tag } from './store.js'
</script>

<section class="section">
  {#if $token}
    {#if $tag}
      <Tag {api}/>
    {:else}
      <Cloud {api}/>
    {/if}
  {:else}
    <Login {api}/>
  {/if}
</section>
