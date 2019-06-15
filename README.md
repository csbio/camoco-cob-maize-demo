# COB Maize Data Demo

Data necessary to create a camoco/cob docker container with prebuilt maize networks.

Builds the version that runs on lovelace for cob.

For more information about COB, see [the main repo](https://github.com/LinkageIO/cob).

## Demo Version

While there is no officially maintained public instance of COB, there is demo server running currently at: [http://lovelace.cs.umn.edu/cob](http://lovelace.cs.umn.edu/cob). This site comes with no garuntee of availibility, so use at your own risk. For a reliable instance, please see the direction below for building and running your own.

## Build Instructions

Just clone and update the git repo and run:

```bash
docker build -t cob .
```

There is also a prebuilt version of this image hosted on docker hub: `linkageio/camoco-cob`. To use this one with the directions below, replace `cob` with `linkageio/camoco-cob` in usage commands below.

## Usage Instructions

To run the built image, run something like this:

```
docker run --rm --name cob-cont --publish 127.0.0.1:50000:50000 cob
```

This will start the container, name it cob, and publish the correct port.

Once it starts, go to `http://localhost:50000` to view it in the browser.

## Systemd Running instructions

To run this as a service, first make sure the image is built on your machine and has the tag `cob`. Then, copy the included `cob.service` file into the `/etc/systemd/system` directory on a linux machine with docker installed.

Then do the following to start and enable it:

```
systemctl daemon-reload
systemctl enable cob.service
systemctl start cob.service
```

This will give you a persistent autostarting instance of cob.

If you have made a new build, run this to restart it with the latest version:

```
systemctl restart cob.service
```

## Contact

This is provided by the efforts of the Myers Lab at the University of Minnesota. For more information see [the lab website](http://csbio.cs.umn.edu/index.html).
