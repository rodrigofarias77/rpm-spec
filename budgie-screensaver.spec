Name: budgie-screensaver
Version: 5.0.1
Release: 1%{?dist}
Summary: Budgie Screensaver is a fork of old gnome screensaver for purposes of providing an authentication prompt on wake

License: GPL
URL: https://github.com/BuddiesOfBudgie/budgie-screensaver

BuildRequires: dbus-glib-devel gcc gnome-desktop3-devel intltool meson pam-devel

Requires: dbus-glib gnome-desktop3 libgnomekbd

%description
Budgie Screensaver is a fork of gnome-screensaver intended for use with Budgie Desktop and is similar in purpose to other screensavers such as MATE Screensaver.

%prep
git clone https://github.com/BuddiesOfBudgie/budgie-screensaver .
git reset --hard 9ec7cf07a92d28c3958884f019bb58039f4b3596

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
