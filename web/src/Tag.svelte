<script>
    import { token, tag } from './store.js'
    export let api;
    let api1 = api; // temp
    let newURL;
    function addURL() {
        tag.set("")
    }
</script>

<div id="container">
    <h1 class="title">{$tag}</h1>
    <div class="field">
        <label for="url" class="label">New URL</label>
        <div class="control">
            <input size="20" id="url" class="input" type="text" placeholder="URL" bind:value={newURL}>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button" on:click={addURL}>Add URL</button>
        </div>       
        <div class="control">
          <button class="button" on:click={() => token.set("")}>Logout</button>
        </div>
    </div>
</div>
