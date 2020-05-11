Name: gfxtablet
Version: 1.5
Release: 1%{?dist}
Summary: Draw on your PC via your Android device

License: MIT
URL: https://github.com/rfc2822/GfxTablet
Source0: https://github.com/rfc2822/GfxTablet/archive/android-app-1.4-linux-driver-1.5.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: g++

%define debug_package %{nil}

%description
Draw on your PC via your Android device

%prep
%setup -q -n GfxTablet-android-app-1.4-linux-driver-1.5

%build
cd driver-uinput
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp driver-uinput/networktablet %{buildroot}/%{_bindir}

ls %{buildroot}/%{_bindir}


%check

%files
%{_bindir}/*

%changelog
* Mon May 11 2020 Jiri Marsicek <jiri.marsicek@gmail.com>  - 1.5-1
- Initial import of android-app-1.4-linux-driver-1.5
