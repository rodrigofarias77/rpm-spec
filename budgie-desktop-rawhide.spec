Name: budgie-desktop
Version: 10.5.2.16
Release: 1%{?dist}
Summary: The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user

License: GPL and LGPL
URL: https://github.com/solus-project/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel cmake gcc git gnome-bluetooth-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel graphene-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: accountsservice gnome-session gnome-settings-daemon librsvg2

Recommends: gnome-control-center gnome-screensaver network-manager-applet

%description

%prep
git clone --depth=100 https://github.com/solus-project/budgie-desktop.git .
git reset --hard ff84056373980a97a11740fdb0296dc637c61425
git submodule update --init

%build
%meson
%meson_build

%install
%meson_install

%files
%config %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*

%exclude %{_datadir}/gir-1.0
%exclude %{_datadir}/vala
%exclude %{_includedir}
%exclude %{_libdir}/lib*.so
%exclude %{_libdir}/pkgconfig

%changelog
