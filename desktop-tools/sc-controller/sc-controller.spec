%{!?__python2: %global __python2 /usr/bin/python2}

Summary:       User-mode driver and GTK3 based GUI for Steam Controller
Name:          sc-controller
Version:       0.4.5
Release:       2
License:       GPL-2.0-only
Group:         Amusements/Games/Other
URL:           https://github.com/kozec/sc-controller
Source:        https://github.com/kozec/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Vendor:        Kozec <kozec at kozec dot com>
Packager:      Kozec <kozec at kozec dot com>


### Requires: python >= 2.7
%if %{defined fedora}
Requires: python-setuptools, python-gobject, gtk3, gnome-python2-rsvg, pylibacl, python-evdev
%else
Requires: python-setuptools, python-gobject, libgtk-3-0, typelib-1_0-Gtk-3_0, typelib-1_0-Rsvg-2_0, python-evdev, python-pylibacl, linux-glibc-devel, python-gobject-common-devel
%endif
BuildRequires: gcc, python-devel, desktop-file-utils

%description
Application allowing to setup, configure and use Steam Controller
without using Steam client.

%prep
%setup

%build
python2 -B setup.py build

%install
python2 setup.py install --root=%{buildroot} -O1
[ -e %{buildroot}/usr/share/applications/sc-controller.desktop.orig ] && rm %{buildroot}/usr/share/applications/sc-controller.desktop.orig

sed -i 's~^#!/usr/bin/python$~#!/usr/bin/python2~' %{buildroot}/usr/bin/*

# mkdir -p %{buildroot}%{_udevrulesdir}
# install -m644 /home/abuild/rpmbuild/SOURCES/99-sc-controller.rules %{buildroot}%{_udevrulesdir}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
/usr/bin/*

%ifarch x86_64
/usr/lib64/python2.7/site-packages/scc
/usr/lib64/python2.7/site-packages/*.so
/usr/lib64/python2.7/site-packages/*.egg-info
%else	# ifarch x86_64
/usr/lib/python2.7/site-packages/scc
/usr/lib/python2.7/site-packages/*.so
/usr/lib/python2.7/site-packages/*.egg-info
%endif	# ifarch x86_64

/usr/lib/udev/rules.d/*
/usr/share/icons/*
/usr/share/applications/*
/usr/share/pixmaps/*
/usr/share/mime/packages/*
/usr/share/scc
