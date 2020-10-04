<script>
    import { token, tag } from './store.js'
    import { onMount } from 'svelte'
    export let api;

    let URLs = []
    let newURL = "";
    let select = -1
    
    async function edit(op, url) {
        if(url.trim() == "") {
          alert("Please specify URL")
          return
        }
        let val = {
            token: $token,
            tag: $tag,
            url: url
        }
        await fetch(api+"/bookmark/"+op, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(val)
        })
        load()
    }

    function delURL() {
      if(select < 0) {
       alert("Please select URL to delete")
       return
      }
      edit("del", URLs[select])
    }

    async function load() {
        let res = await fetch(api+"/bookmark/tag?token="+$token+"&tag="+encodeURI($tag))
        res = await res.json()
        URLs = res[$tag]
        console.log(URLs)
    }

    onMount(load)
</script>

<div id="container">
    <h1 class="title">{$tag}</h1>
  {#if URLs.length}
    <table class="table">
        <thead>
          <tr>
            <th></th>
            <th>URL</th>
          </tr>
        </thead>
        <tbody>
          {#each URLs as url, i }
          <tr>
            <th><input type="radio" bind:group={select} value={i}></th>
            <td><a href="{url}">{url}</a></td>
          </tr>
          {/each}
        </tbody>
    </table>
  {/if}

    <div class="field">
        <label for="url" class="label">New URL</label>
        <div class="control">
            <input size="20" id="url" class="input" type="text" placeholder="URL" bind:value={newURL}>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button" on:click={() => { edit("add", newURL) ; newURL=""}}>Add URL</button>
        </div>
        <div class="control">
          <button class="button" on:click={delURL}>Delete URL</button>
        </div>
        <div class="control">
            <button class="button" on:click={() => tag.set("")}>Tags</button>
          </div>       
        <div class="control">
          <button class="button" on:click={() => token.set("")}>Logout</button>
        </div>
    </div>
</div>
