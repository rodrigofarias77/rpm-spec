Name: budgie-desktop-view
Version: 1.2.0
Release: 1%{?dist}
Summary: Budgie Desktop View is the official Budgie desktop icons application / implementation

License: Apache
URL: https://github.com/BuddiesOfBudgie/budgie-desktop-view

BuildRequires: meson gtk3-devel intltool vala

Requires: budgie-desktop

%description

%prep
git clone https://github.com/BuddiesOfBudgie/budgie-desktop-view.git .
git reset --hard 1f30d69f326ef10563165e1ce9abbc0fd94bd716

%build
%meson
%meson_build

%install
%meson_install

%files
%config %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*

%changelog
