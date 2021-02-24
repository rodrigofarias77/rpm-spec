Build `budgie-desktop` for Fedora 33 in a Docker container:
```
docker build -t budgie-desktop:33 --build-arg={version=33,spec=budgie-desktop.spec} .
docker run -v $PWD:/mnt budgie-desktop:33
```
The `.rpm` file will be placed in the current directory.
