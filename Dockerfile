ARG version=latest

FROM fedora:$version

WORKDIR /root

ARG spec

ENV local project.spec

COPY $spec $local

RUN dnf -y install fedora-packager && dnf -y builddep $local && dnf clean all

RUN rpmdev-setuptree

ENTRYPOINT rpmbuild -bb $local && cp -v rpmbuild/RPMS/x86_64/*.rpm /mnt

# vim: filetype=dockerfile
