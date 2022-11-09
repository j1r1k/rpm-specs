%global gitsnapshot 1
%if 0%{?gitsnapshot}
%global snapcommit 3c1590786518e9acca33c250660ad21cae565acd
%global snapcount 81
%global shortcommit %(c=%{snapcommit}; echo ${c:0:7})
%global snapver .git.%{snapcount}.%{shortcommit}
%endif

%global tagver 1.2.9

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif

%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
%bcond_without gtk4
%endif

%global nm_version          1.2.0
%global gtk3_version        3.4.0
%global openconnect_version 7.00

Summary:   NetworkManager VPN plugin for openconnect
Name:      NetworkManager-openconnect
Version:   %{tagver}%{?snapver}
Release:   0%{?dist}
License:   GPLv2+ and LGPLv2
URL:       http://www.gnome.org/projects/NetworkManager/
%if 0%{?gitsnapshot}
Source0:   https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{snapcommit}/%{name}-%{snapcommit}.tar.gz
%else
Source0:   https://www.infradead.org/openconnect/download/%{name}-%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libnm) >= %{nm_version}
BuildRequires: pkgconfig(libnma) >= %{nm_version}
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: intltool gettext libtool
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(openconnect) >= %{openconnect_version}
BuildRequires: pkgconfig(gcr-3) >= 3.4
%if %{with libnm_glib}
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
%endif
%if %with gtk4
BuildRequires: pkgconfig(gtk4) >= 4.0
BuildRequires: pkgconfig(libnma-gtk4) >= 1.8.33
%endif
BuildRequires: pkgconfig(webkit2gtk-4.0)

Requires: NetworkManager   >= %{nm_version}
Requires: openconnect      >= %{openconnect_version}
Requires: dbus-common
Obsoletes: NetworkManager-openconnect < 1.2.3-0

Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating the openconnect VPN software
with NetworkManager and the GNOME desktop

%package gnome
Summary: NetworkManager VPN plugin for OpenConnect - GNOME files

Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: NetworkManager-openconnect < 1.2.3-0

%description gnome
This package contains software for integrating VPN capabilities with
the OpenConnect client with NetworkManager (GNOME files).

%prep
%if 0%{?gitsnapshot}
%autosetup -p1 -n %{name}-%{snapcommit}
NOCONFIGURE=x ./autogen.sh
%else
$autosetup -p1
if [ ! -x configure ]; then
    NOCONFIGURE=x ./autogen.sh
fi
%endif

%build
%configure \
        --enable-more-warnings=yes \
        --disable-static \
%if %{with libnm_glib}
        --with-libnm-glib \
%else
        --without-libnm-glib \
%endif
%if %with gtk4
        --with-gtk4 \
%endif
        --with-dist-version=%{version}-%{release}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang %{name}

%pre
%{_sbindir}/groupadd -r nm-openconnect &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d / -M \
                     -c 'NetworkManager user for OpenConnect' \
                     -g nm-openconnect nm-openconnect &>/dev/null || :

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/usr/bin/update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
      %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
/usr/bin/update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
      %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
%endif

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%{_datadir}/dbus-1/system.d/nm-openconnect-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_libexecdir}/nm-openconnect-service
%{_libexecdir}/nm-openconnect-service-openconnect-helper
%doc AUTHORS ChangeLog NEWS
%license COPYING

%files gnome
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
%{_datadir}/metainfo/network-manager-openconnect.metainfo.xml

%if %with gtk4
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-openconnect-editor.so
%endif

%if %{with libnm_glib}
%{_libdir}/NetworkManager/libnm-*-properties.so
%{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%endif


%changelog
* Sat Apr 30 2022 David Woodhouse <dwmw2@infradead.org> - %{version}-%{release}
- Autopackaging for COPR
