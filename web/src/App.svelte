<script>
  export let api;
  import Login from './Login.svelte'
  import Cloud from './Cloud.svelte'
  import { token } from './store.js'
  
  function logout() {
    token.set("")
  }
</script>

<section class="section">
  {#if $token}
    <Cloud {api}/>
    <button class="button" on:click={logout}>Logout</button>
  {:else}
    <Login {api}/>
  {/if}
</section>