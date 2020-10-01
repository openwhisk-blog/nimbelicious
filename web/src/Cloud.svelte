<script>
    export let api;
    let api1 = api; // temp

    import { token, tag } from './store.js'
    import { onMount } from 'svelte'
    import WordCloud from 'wordcloud';
  
    let newTag;

    let list = [
          ['Michele', 10, 'http://google.com?q=foo'], 
          ['Mirella', 8, 'http://google.com?q=bar'],
          ['Laura',   8, 'http://google.com?q=bar'],
          ['Massimo', 6, 'http://google.com?q=bar']
    ]

    onMount(() => {
        WordCloud(document.getElementById('canvas'), {
            list: list, 
            gridSize: 8,
            weightFactor: 4,
            origin: [400, 300],
            fontFamily: 'Times, serif',
            color: 'random-light',
            backgroundColor: '#000',
            shuffle: false,
            rotateRatio: 0,
            hover: function(item, rect) {
                console.log(rect)
                let marker = document.getElementById("marker")
                if(rect) {
                    marker.setAttribute("x", rect.x)
                    marker.setAttribute("y", rect.y)
                    marker.setAttribute("width", rect.w)
                    marker.setAttribute("height", rect.h)
                    marker.setAttribute("display", "true")
                } else {
                    marker.setAttribute("display", "none")
                }
            },
            click: function(item) {
                tag.set(item[0])
            },
            backgroundColor: '#001f00'
        })
    })

    function addTag() {
        tag.set(newTag)
    }


</script>
<div class="container">
   <div id="tags">
     <canvas width="600" height="400" id="canvas"></canvas>
     <svg id="overlay">
       <rect id="marker" x="0" y="0" width="600" height="400"
          style="stroke: #009900;stroke-width: 3;fill: none;" />
     </svg>
   </div>
</div>
<div id="container">
    <div class="field">
        <label for="tag" class="label">New Tag</label>
        <div class="control">
            <input size="20" id="tag" class="input" type="text" placeholder="Tag" bind:value={newTag}>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button" on:click={addTag}>Add Tag</button>
        </div>       
        <div class="control">
            <button class="button" on:click={() => token.set("")}>Logout</button>
        </div>
    </div>
</div>

<style>
#tags {
    width: 600px;
    height: 400px;
    position: relative;
}
#canvas,
#overlay {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
}
#overlay {
    z-index: 10;
    pointer-events: none;
}
</style>
