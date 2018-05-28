%global _enable_debug_package 0
%global debug_package %{nil}

Name:           efitools
Version:        1.8.1
Release:        0%{?dist}
Summary:        Tools for manipulating UEFI secure boot platforms

License:        GPLv2
URL:            http://git.kernel.org/cgit/linux/kernel/git/jejb/efitools.git

Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/%{name}-%{version}.tar.gz
Source1:        https://github.com/tianocore/edk2/blob/master/EdkShellBinPkg/FullShell/X64/Shell_Full.efi

BuildRequires:  gnu-efi-devel >= 3.0q sbsigntools openssl-devel openssl help2man perl(File::Slurp) git
Requires:       sbsigntools openssl parted dosfstools mtools

%define efidir %{_datadir}/efitools/efi

%description
Tools for manipulating keys and binary signatures on UEFI secure boot platforms.

%prep
%autosetup -S git_am

%build
make

%install
%make_install

# docs should not be installed under /usr/share/efitools
rm -f %{buildroot}/%{_datadir}/efitools/COPYING
rm -f %{buildroot}/%{_datadir}/efitools/README

# the LockDown binary has the wrong keys in it
rm -f %{buildroot}/%{efidir}/LockDown.efi

# install EFI Shell
install -p -m 0644 %{SOURCE1} %{buildroot}/%{efidir}/

# provide empty dirs for keys and USB image built by mkusb script
install -d %{buildroot}/%{efidir}/keys
install -d %{buildroot}/%{efidir}/usb

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*
%{efidir}/*
%doc COPYING
%doc README

%changelog
* Thu May 10 2018 jiri.marsicek@gmail.com - 1.8.1-0
- Bump to 1.8.1

* Mon Feb 05 2018 jiri.marsicek@gmail.com - 1.8.0-1
- Bump to 1.8.0

* Thu Sep 17 2015 Michal Sekletar <msekleta@redhat.com>
- import efitools-1.5.3
