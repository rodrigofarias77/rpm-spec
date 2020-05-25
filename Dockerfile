ARG version=latest

FROM fedora:$version

ARG spec

WORKDIR /root

RUN dnf -y install fedora-packager && dnf clean all

ENV local project.spec

COPY $spec $local

RUN dnf -y builddep $local && dnf clean all

RUN rpmdev-setuptree

ENTRYPOINT rpmbuild -bb $local && cp -v rpmbuild/RPMS/x86_64/*.rpm /mnt

# vim: filetype=dockerfile
