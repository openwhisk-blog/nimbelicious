<script>
  export let api;
  import Login from './Login.svelte'
  import Cloud from './Cloud.svelte'
  import Tag from './Tag.svelte'
  import { token, tag } from './store.js'
  
  // check token
  let hs = location.href.split("?")
  if(hs.length > 1) {
    let qs = hs[1].split(";")
    if(qs.length >1) {
      let ttoken = spl1.shift()
      let turl = spl1.join(";")
      fetch(api+"/bookmark/login?token="+ttoken)
      .then((res) => { 
         if(res.ok) {
           token.set(ttoken)
           url.set(turl)
         }
      })
      
    }
  }

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
