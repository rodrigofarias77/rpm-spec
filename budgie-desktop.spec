Name: budgie-desktop
Version: 10.5.1
Release: 29%{?dist}
Summary: The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user

License: GPL and LGPL
URL: https://github.com/solus-project/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel cmake git gnome-bluetooth-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: gnome-control-center gnome-menus gnome-screensaver gnome-session ibus libpeas librsvg2 libwnck3 mutter network-manager-applet

%description

%prep
git clone --depth=10 https://github.com/solus-project/budgie-desktop.git
cd %{name}
git reset --hard c4dbb0636036f09fdf9ad52efd3b23bd3ef61706
git submodule update --init

%build
cd %{name}
%meson
%meson_build

%install
cd %{name}
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
