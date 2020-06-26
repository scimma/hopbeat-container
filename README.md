# hopbeat-container

This repository is used to buiild a container for 
a simple HOP-based applet that sends a message every
30 seconds.

## Build

```
make 
```

## Push to Amazon ECS

This should only be done via github CI.

```
make push
```

## TODO

1. setup github CI
2. modify the makefile to use environment variables from github CI to determine the versions/tags for pushing to AWS ECR.
3. ``runHopBeat.py`` could be made more robust.
4. Export some metrics to influxdb.
5. Write a *liveness* testing script for use by the EKS deployment.
