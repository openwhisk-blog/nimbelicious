<script>
  export let api;
  import Login from './Login.svelte'
  import Cloud from './Cloud.svelte'
  import Tag from './Tag.svelte'
  import { token, tag, url } from './store.js'

  // autologin
  let hs = location.href.split("?")
  console.log(hs)
  if(hs.length > 1) {
    let qs = hs[1].split(";")
    let tk = qs.shift()
    fetch(api+"/bookmark/login?token="+tk)
    .then(async (res) => {
      console.log(res)
      let body = await res.json()
      console.log(body)
      if(res.ok && body.ok) 
        token.set(tk)
    })
    if(qs.length>0)
      url.set(qs.join(";"))
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
