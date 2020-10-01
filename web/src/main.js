import 'bulma/css/bulma.min.css';
import App from './App.svelte';

// calculate api server location 
let apiserver = "apigcp.nimbella.io"
let pos = location.hostname.indexOf(apiserver)
let namespace = ""

if(location.hostname == "localhost")  {
	// development namespace - start slash required
	namespace = "/micheles-3bjkqg0vpyb"
} else if(pos != -1) {
   // nimbella deployment
   namespace = "/" + location.hostname.substring(0,pos) 
}  else {
  // proxified deployment
  apiserver = location.hostname
}

apiserver = "https://"+apiserver + "/api/v1/web"+ namespace
console.log(apiserver)

const app = new App({
	target: document.body,
	props: { "api": apiserver }
});

export default app;
