ARG version

FROM fedora:$version

WORKDIR /root

RUN dnf -y upgrade && dnf -y install fedora-packager

ARG spec

COPY $spec .

RUN dnf -y upgrade && dnf -y builddep $spec

RUN rpmdev-setuptree

ENV spec=$spec

ENTRYPOINT rpmbuild -bb /mnt/$spec && cp -v rpmbuild/RPMS/x86_64/*.rpm /mnt
