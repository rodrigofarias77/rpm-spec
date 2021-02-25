Name: gnome-screensaver
Version: 3.6.1.9
Release: 2%{?dist}
Summary: Legacy GNOME screensaver

License: GPL
URL: https://wiki.gnome.org/Projects/GnomeScreensaver

BuildRequires: dbus-glib-devel git gnome-common gnome-desktop3-devel gtk3-devel intltool pam-devel which

Requires: dbus-glib gnome-desktop3 libgnomekbd

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%prep
git clone https://gitlab.gnome.org/Archive/gnome-screensaver.git .
git checkout gnome-3-6
git diff ...master :\!po | git apply -v # non-translation changes from master
curl -Ls https://raw.githubusercontent.com/rodrigofarias77/rpm-spec/master/gnome-screensaver.patch | git apply -v -
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
