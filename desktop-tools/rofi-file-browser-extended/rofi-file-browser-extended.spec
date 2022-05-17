%define debug_package %{nil}

Name:           rofi-file-browser-extended
Version:        1.3.1
Release:        1
Summary:        Use rofi to quickly open files
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/marvinkreis/%{name}
Source0:        https://github.com/marvinkreis/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake cairo-devel gcc gcc-c++ make
BuildRequires:  rofi-devel >= 1.5
Requires:       rofi >= 1.5

%description
rofi-file-browser-extended is a configurable file browser plugin for rofi. Its main use case is to quickly open files without having to open a window to navigate to the file.

%prep
%setup -q

%build
pwd
ls
cmake .
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1.gz
%{_libdir}/rofi/filebrowser.so

%changelog
* Tue May 17 2022 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.3.1-1
- Update to v1.3.1

* Tue Nov 09 2021 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.2.0-1
- Initial spec

