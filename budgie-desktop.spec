Name: budgie-desktop
Version: 10.5.2.13
Release: 2%{?dist}
Summary: The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user

License: GPL and LGPL
URL: https://github.com/solus-project/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel cmake git gnome-bluetooth-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: gnome-menus gnome-session gnome-settings-daemon ibus-libs libpeas librsvg2 libwnck3 mutter

Recommends: gnome-control-center gnome-screensaver network-manager-applet

%description

%prep
git clone --depth=100 https://github.com/solus-project/budgie-desktop.git .
git reset --hard 6d020359f1cb3b40132cd30385da078b1a9bbda4
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
