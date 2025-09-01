Name:           fcitx5-bamboo
Version:        1.0.8
Release:        1%{?dist}
Summary:        A packaged release of upstream fcitx5-bamboo, a Vietnamese IME
License:        LGPL-2.1+
URL:            https://github.com/fcitx/fcitx5-bamboo
Source:         %{name}-%{version}
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  libappstream-glib
BuildRequires:  fcitx5-devel
BuildRequires:  golang

%description
Bamboo (Vietnamese Input Method) engine support for Fcitx

Based on https://github.com/BambooEngine/bamboo-core

Released under LGPLv2.1+

%prep
%autosetup -S git
git submodule update --init --recursive

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/fcitx5/libbamboo.so
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Bamboo.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/fcitx5-bamboo.mo
%{_datadir}/fcitx5/inputmethod/bamboo.conf
%{_datadir}/fcitx5/addon/bamboo.conf
%{_datadir}/icons/hicolor/scalable/apps/fcitx_bamboo.svg
%{_datadir}/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_bamboo.svg
%{_datadir}/fcitx5/bamboo/vietnamese.cm.dict

%changelog
%autochangelog
