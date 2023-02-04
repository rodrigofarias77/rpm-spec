Build `budgie-desktop` for Fedora 36 in a Docker container:
```
docker build -t budgie-desktop:36 --build-arg spec=budgie-desktop-36.spec --build-arg version=36 --pull .
docker run -v $PWD:/mnt --rm budgie-desktop:36
```
The `.rpm` file will be placed in the current directory.
