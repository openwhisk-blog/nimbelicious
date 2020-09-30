import 'bulma/css/bulma.min.css';
import App from './App.svelte';

let apiserver = "apigcp.nimbella.io"
let pos = location.hostname.indexOf(apiserver)
let namespace = "micheles-3bjkqg0vpyb"

if(location.hostname == "localhost")  {
	// do nothing
} else if(pos != -1) {
   namespace = location.hostname.substring(0,pos)
}  else {
  // todo
}

apiserver = "https://"+apiserver + "/api/v1/web/"+ namespace
console.log(apiserver)

const app = new App({
	target: document.body,
	props: { "api": apiserver }
});

export default app;
