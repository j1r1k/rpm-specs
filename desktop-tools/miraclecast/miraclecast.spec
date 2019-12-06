Name: miraclecast
Version: 0.1
Release: 1.4111333%{?dist}
Summary: Connect external monitors to your system via Wifi-Display specification also known as Miracast

License: LGPL
URL: https://github.com/albfan/%{name}
Source0: https://github.com/albfan/%{name}/tarball/41113335211463e122f7e5f782274c84752703c9#/%{name}-%{version}.tar.gz

BuildRequires: gcc glib2-devel automake libtool systemd-devel libudev-devel readline-devel
Requires: systemd >= 221 gstreamer
Recommends: bash-completion

%description

%prep
%setup -q -n albfan-%{name}-4111333

%build
ls -l
./autogen.sh c --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --includedir=%{_includedir}
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/gstplayer
%{_bindir}/miracle-dhcp
%{_bindir}/miracle-gst
%{_bindir}/miracle-omxplayer
%{_bindir}/miracle-sinkctl
%{_bindir}/miracle-uibcctl
%{_bindir}/miracle-wifictl
%{_bindir}/miracle-wifid
%{_bindir}/miracled
%{_bindir}/uibc-viewer
%{_datadir}/bash-completion/completions/miracle-sinkctl
%{_datadir}/bash-completion/completions/miracle-wifictl
%{_datadir}/bash-completion/completions/miracle-wifid
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.miracle.conf

%changelog
* Sat Nov 30 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.1-4111333-1
- Initial import

