# Based on https://copr-dist-git.fedorainfracloud.org/cgit/larsks/watchman/watchman.git/tree/watchman.spec
Name:           watchman
Version:        4.9.0
Release:        0%{?dist}
Summary:        Watches files and records, or triggers actions, when they change.

Group:          Development/Tools
License:        Apache 2.0
URL:            https://facebook.github.io/watchman
Source0:        https://github.com/facebook/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        watchman-tmpfiles.conf

BuildRequires:  git, libtool, openssl-devel, pcre-devel, systemd

%description
Watches files and records, or triggers actions, when they change.

%package python3
Summary: Python bindings for Watchman, a file monitoring service

BuildRequires:  python3-devel python3-setuptools

%description python3
Watches files and records, or triggers actions, when they change.

This package provides Python bindings for Watchman.

%prep
%autosetup -S git
./autogen.sh

%build
%configure --with-python=%{_bindir}/python3 --enable-statedir=%{_rundir}/%{name}
make %{?_smp_mflags} CXXFLAGS="-Wno-error=format-truncation -fPIC"

%install
%make_install
install -m 755 -d %{buildroot}%{_tmpfilesdir}
install -m 644 %{S:1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}
rm -f %{buildroot}%{_rundir}/%{name}/.not-empty


%files
%doc README.markdown
%license LICENSE
%{_bindir}/watchman
%{_bindir}/watchman-make
%{_bindir}/watchman-wait
%{_tmpfilesdir}/watchman.conf
%ghost %{_rundir}/%{name}


%files python3
%{python3_sitearch}/pywatchman-1.4.0-py%{python3_version}.egg-info/
%{python3_sitearch}/pywatchman/


%changelog
* Thu Oct 18 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - -
- import watchmen-4.9.0

