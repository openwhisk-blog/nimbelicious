import 'bulma/css/bulma.min.css';
import App from './App.svelte';

// calculate api server location 
let apiserver = "apigcp.nimbella.io"
let namespace = ""
let path = "/api/v1/web"
let pos = location.hostname.indexOf(apiserver)

if(location.hostname == "localhost")  {
  // development namespace 
  // change this to your own for development 
  // start slash is required
	namespace = "/msciabar-zc3thebgxgh"
} else if(pos != -1) {
   // nimbella deployment
   namespace = "/" + location.hostname.substring(0,pos-1) 
}  else {
  // proxified deployment
  apiserver = location.hostname
  path = "/.netlify/nimbella"
}

apiserver = "https://"+ apiserver + path + namespace
console.log(apiserver)

const app = new App({
	target: document.body,
	props: { "api": apiserver }
});

export default app;
