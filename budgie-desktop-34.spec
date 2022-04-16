Name: budgie-desktop
Version: 10.6.20
Release: 2%{?dist}
Summary: Budgie Desktop is a familiar, modern desktop environment

License: GPL and LGPL
URL: https://github.com/BuddiesOfBudgie/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel cmake gcc git gnome-bluetooth-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel graphene-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: accountsservice gnome-session gnome-settings-daemon librsvg2

Recommends: budgie-screensaver gnome-control-center network-manager-applet

%description
The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user.

%prep
git clone --depth=100 https://github.com/BuddiesOfBudgie/budgie-desktop.git .
git reset --hard be79b9c2065bcdccd1786f1f193522c5e6d5845b
git submodule update --init
git revert -n 314132131a46b9ba57b68848c5b32a475034c917
sed -i -r '/assert.(budgie|gnome)_screensaver/d; /^dep_vala/s/0.52.5/0.48.0/' meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/*
%{_datadir}/*
%{_includedir}/*
%{_libdir}/*
%{_sysconfdir}/*
%exclude %{_libdir}/pkgconfig
