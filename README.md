# hopbeat-container

This repository is used to buiild a container for 
a simple HOP-based applet that sends a message every
30 seconds.

## Build

```
make 
```

## Release

Pushing to AWS ECR is handled via a github workflow. To push a container based on
the current master branch to AWS ECR with 
version MAJOR.MINOR.RELEASE (e.g., "0.0.7") do:

```
git tag version-MAJOR.MINOR.RELEASE
git push origin version-MAJOR.MINOR.RELEASE
```

## TODO

1. Maybe export some metrics to influxdb.
2. Write a *liveness* testing script for use by the EKS deployment.
3. Set delay from an environment variable instead of using a fixed 30 seconds.
