Name:           faenza-icon-theme
Version:        1.3.1
Release:        1%{?dist}
Summary:        A scalable icon theme called Faenza

License:        GPLv3
URL:            http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:        https://launchpad.net/~tiheum/+archive/ubuntu/equinox/+files/%{name}_%{version}.tar.gz

%define iconsdir /%{_datadir}/icons

%description
A scalable icon theme called Faenza

%prep
%autosetup -n %{name}-1.3

%install
mkdir -p %{buildroot}/%{iconsdir}
for D in Faenza Faenza-Ambiance Faenza-Dark Faenza-Darker Faenza-Darkest Faenza-Radiance; do
  cp -pr "$D" "%{buildroot}/%{iconsdir}/$D"
done

%files
%{iconsdir}/*

%changelog
* Wed Feb  7 2018 Jiri Marsicek <jiri.marsicek@gmail.com>
- initial import of faenza-icon-theme-1.3.1
