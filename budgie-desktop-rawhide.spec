Name: budgie-desktop
Version: 10.5.3.136
Release: 2%{?dist}
Summary: The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user

License: GPL and LGPL
URL: https://github.com/BuddiesOfBudgie/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel annobin-plugin-gcc cmake gcc git gnome-bluetooth3.34-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel graphene-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: accountsservice gnome-session gnome-settings-daemon librsvg2

Recommends: budgie-screensaver gnome-control-center network-manager-applet

%description

%prep
git clone --depth=100 https://github.com/BuddiesOfBudgie/budgie-desktop.git .
git reset --hard f43e129635f1bb019dad8cc6f6be5f96399461b8
git submodule update --init
curl -s https://patch-diff.githubusercontent.com/raw/BuddiesOfBudgie/budgie-desktop/pull/54.patch | git apply -v -
sed -i -r '/assert.(budgie|gnome)_screensaver/d' meson.build

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
