# How to run Redis + API container


```
docker-compose up -d --build 
```

# How to test caching

First call to endpoint takes significantly longer. Afterwards latency is reduced.

```
http://localhost:5000//universities?country=Germany
```