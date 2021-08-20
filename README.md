# suasana-pi
Kue memantau suasana.

Exporting atmospheric data from a DHT sensor with a Raspberry Pi, so that a Prometheus server in a container can grab them over a wireguard vpn, for a containerized grafana installation to display the room temperature I'm sitting in. KISS.


```
DHT Temperature Sensor <- Raspberry Pi <- Prometheus <- Grafana
 \-----------------------------------/
                 |
            suasana-pi
```
I was told that "suasana" means "atmosphere" in bahasa indonesia. 
