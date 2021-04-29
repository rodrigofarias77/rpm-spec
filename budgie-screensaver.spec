Name: budgie-screensaver
Version: 4.0.0
Release: 2%{?dist}
Summary: Fork of GNOME Screensaver for Budgie 10

License: GPL
URL: https://github.com/getsolus/budgie-screensaver

BuildRequires: dbus-glib-devel git gnome-common gnome-desktop3-devel gtk3-devel intltool pam-devel which

Requires: dbus-glib gnome-desktop3 libgnomekbd

%description
Budgie Screensaver is a fork of gnome-screensaver intended for use with Budgie Desktop and is similar in purpose to other screensavers such as MATE Screensaver.

%prep
git clone https://github.com/getsolus/budgie-screensaver.git .
sed -i '/^auth.*pam_gnome_keyring/s/^/-/' data/budgie-screensaver
./autogen.sh

%build
%configure --with-mit-ext=no
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%doc %{_mandir}/man1/*.1.gz
%{_bindir}/*
%{_datadir}/applications/*
%{_libexecdir}/*
%{_sysconfdir}/pam.d/*
