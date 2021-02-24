Name: gnome-screensaver
Version: 3.6.1
Release: 2%{?dist}
Summary: GNOME Screensaver

License: GPLv2+
URL: http://www.gnome.org

BuildRequires: autoconf automake dbus-devel dbus-glib-devel desktop-file-utils gettext gnome-common gnome-desktop3-devel gtk3-devel intltool libgnomekbd-devel libtool libX11-devel libXext-devel libXinerama-devel libXmu-devel libXScrnSaver-devel libXtst-devel libXxf86vm-devel nss-devel pam-devel systemd-devel xorg-x11-proto-devel

Requires: gnome-keyring-pam gsettings-desktop-schemas redhat-menus

Conflicts: xscreensaver

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%prep
curl -LOs http://download.gnome.org/sources/gnome-screensaver/3.6/gnome-screensaver-%{version}.tar.xz
tar -xf *.tar.xz --strip-components=1
curl -LOs https://raw.githubusercontent.com/rodrigofarias77/rpm-spec/master/gnome-screensaver.patch
patch -p1 < gnome-screensaver.patch
autoreconf -f -i

%build
%configure --with-mit-ext=no --enable-systemd
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/gnome-screensaver.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/*
%{_libexecdir}/*
%{_sysconfdir}/pam.d/*
%doc %{_mandir}/man1/*.1.gz
