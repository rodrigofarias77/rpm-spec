Name: budgie-screensaver
Version: 5.0.2
Release: 2%{?dist}
Summary: Budgie Screensaver is a fork of old gnome screensaver for purposes of providing an authentication prompt on wake

License: GPL
URL: https://github.com/BuddiesOfBudgie/budgie-screensaver

BuildRequires: dbus-glib-devel gcc git gnome-desktop3-devel intltool libgnomekbd-devel meson pam-devel

Requires: dbus-glib gnome-desktop3 libgnomekbd

%description
Budgie Screensaver is a fork of gnome-screensaver intended for use with Budgie Desktop and is similar in purpose to other screensavers such as MATE Screensaver.

%prep
git clone https://github.com/BuddiesOfBudgie/budgie-screensaver .
git reset --hard 1e0dca5f2e83066de37c2d113f5d288a9c0efb0e
sed -i '/^auth.*pam_gnome_keyring/s/^/-/' data/budgie-screensaver

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/*
%{_datadir}/*
%{_libexecdir}/*
%{_sysconfdir}/*
