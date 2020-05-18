ARG version=latest

FROM fedora:$version

WORKDIR /root

ARG spec

COPY $spec .spec

RUN dnf -y install fedora-packager && dnf -y builddep .spec && dnf clean all

RUN rpmdev-setuptree

ENTRYPOINT rpmbuild -bb .spec && cp -v rpmbuild/RPMS/x86_64/*.rpm /mnt

# vim: filetype=dockerfile
