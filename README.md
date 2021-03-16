# hopbeat-container

This repository is used to buiild a container for 
a simple HOP-based applet that sends a message every
30 seconds.

## Environment

Several environment variables affect the behavior of the hopbeat-client:

* `HOP_SECRET`   - The name of the AWS secret containing the credentails for connecting to the HOP server. Default: `dev-gcn2hop-hopcreds`.
* `HOP_REGION`   - The region in which the secret is stored. Default: `us-west-2`.
* `HOP_SERVER`   - The name of the HOP server to which to send messages. Default: `dev.hop.scimma.org:9092`.
* `HOP_INTERVAL` - The number of seconds to sleep after sending a message before sending the next message. Default: 30.

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
