Build `budgie-desktop` for Fedora 35 in a Docker container:
```
docker build -t budgie-desktop:35 --build-arg spec=budgie-desktop.spec --build-arg version=35 .
docker run -v $PWD:/mnt budgie-desktop:35
```
The `.rpm` file will be placed in the current directory.
