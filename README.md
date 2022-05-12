# GKE-demo

- Provisions a Kubernetes cluster in GKE

1. Create a project on Google Cloud
2. Run src/gcloud/gcloud_auth.sh
3. ```pulumi stack init```
   1. select defaults
4. ```pulumi up```
5. Run src/gcloud_create_nat.sh
6. Run src/kube/setup_config.sh
7. Test on a browser:
   1. ```http://35.185.199.254/headers```
   2. Something like this should display:
```
headers: {
      Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      Accept-Encoding: "gzip, deflate",
      Accept-Language: "en-US,en;q=0.9",
      Cache-Control: "no-cache",
      Dnt: "1",
      Host: "35.185.199.254",
      Pragma: "no-cache",
      Sec-Gpc: "1",
      Upgrade-Insecure-Requests: "1",
      User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
      X-B3-Parentspanid: "fd11ff3306fd6453",
      X-B3-Sampled: "1",
      X-B3-Spanid: "168e5f1b2f90ffe8",
      X-B3-Traceid: "a30612c27242817dfd11ff3306fd6453",
      X-Envoy-Attempt-Count: "1",
      X-Envoy-Internal: "true",
      X-Forwarded-Client-Cert: "By=spiffe://cluster.local/ns/gke-demo/sa/httpbin;Hash=34e7fd2fa298fee84e139a53965766d55513e861a48ac1974bf5478d765be922;Subject="";URI=spiffe://cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account"
   }
}
```
8. Profit