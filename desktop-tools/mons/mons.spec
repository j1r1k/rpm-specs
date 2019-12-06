Name:           mons
Version:        0.8.2
Release:        3%{?dist}
Summary:        POSIX Shell script to quickly manage three monitors on X

License:        MIT
URL:            https://github.com/Ventto/mons
Source0:        https://github.com/Ventto/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/Ventto/libshlist/archive/v1.1.tar.gz

Requires:       xorg-x11-server-utils

%description
Mons is a Shell script to quickly manage 2-monitors display using xrandr

%prep
%setup -q -T -b 0
%setup -q -T -a 1 -D
mv libshlist-1.1/* libshlist/
rmdir libshlist-1.1

%install
%make_install

%files
%license LICENSE
%{_bindir}/*
%{_mandir}/*
%{_usr}/lib/*

%changelog
* Tue Feb  6 2018 Jiri Marsicek <jiri.marsicek@gmail.com>
- initial import of mons-0.8.2
