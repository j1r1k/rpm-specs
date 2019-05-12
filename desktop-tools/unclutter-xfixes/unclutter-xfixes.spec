Name: unclutter-xfixes
Version: 1.5
Release: 1%{?dist}
Summary: Unclutter-xfixes is a rewrite of unclutter using the x11-xfixes extension

License: MIT
URL: https://github.com/Airblader/%{name}
Source0: https://github.com/Airblader/%{name}/archive/v%{version}.tar.gz

BuildRequires: asciidoc, gcc, git, libev-devel, libX11-devel, libXi-devel, libXfixes-devel
Requires: libev, libX11, libXfixes, libXi

%description

#%%global debug_package %%{nil}

%prep
%setup -q


%build
%define debug_package %{nil}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

%files
%license /usr/share/licenses/unclutter/LICENSE
%doc README.md
%{_bindir}/unclutter
%{_mandir}/man1/unclutter.1.gz

%changelog
* Sun May 12 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.5-1
- Initial import from https://copr.fedorainfracloud.org/coprs/nbeernink/unclutter-xfixes/

