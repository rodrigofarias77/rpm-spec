Build `budgie-desktop` for Fedora 32 in a Docker container:
```
docker build -f budgie-desktop.docker -t budgie-desktop:32 --build-arg version=32 .
docker run -v $PWD:/mnt budgie-desktop:32
```
The `.rpm` file will be copied to the current directory.
