Name: budgie-desktop
Version: 10.5.2.11
Release: 3%{?dist}
Summary: The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user

License: GPL and LGPL
URL: https://github.com/solus-project/budgie-desktop

BuildRequires: accountsservice-devel alsa-lib-devel cmake git gnome-bluetooth-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel gtk3-devel gtk-doc ibus-devel intltool libnotify-devel libpeas-devel libuuid-devel libwnck3-devel mesa-libEGL-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala

Requires: gnome-control-center gnome-menus gnome-session ibus libpeas librsvg2 libwnck3 mutter network-manager-applet

%description

%prep
git clone --depth=100 https://github.com/solus-project/budgie-desktop.git
cd %{name}
git reset --hard b8d84afc9f5cc866449918b1ab2e80910a52d70d
git submodule update --init
curl -s https://github.com/solus-project/budgie-desktop/commit/{0e667b645d2b388a0431c8fb67b7253bd05c08e5,6ca50bc24b20a29b8bdb652be8ed60f1ba3dcd43,86b1d48e6495eabeb2e551b99e42a0e78975e5f1,e8355a5cc3c9d0266daf3ec207fe38aa2fb6b996,852e8c39b0ab2c2403e05c557ed7c671045192bb,ea547498dae001ce3631e5118374efac6255e2e8}.diff | git apply -v -

%build
cd %{name}
%define _lto_cflags %{nil}
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
