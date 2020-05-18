Build `budgie-desktop` for Fedora 32 in a Docker container:
```
docker build -t budgie-desktop:32 --build-arg={version=32,spec=budgie-desktop.spec} .
docker run -v $PWD:/mnt budgie-desktop:32
```
The `.rpm` file will be placed in the current directory.
