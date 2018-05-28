%global _hardened_build 1

Name:           sbsigntools
Version:        0.9.1

Release:        2%{?dist}
Summary:        EFI binary signing tools

License:        GPLv3
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/

Source0:        %{name}.combined-%{version}.tar.gz
# upsream source tarball does not contain ccan source submodule
# create combined tarball by invoking ./generate-tarball.sh $VERSION
Source1:        generate-tarball.sh
# used in generate-tarball.sh
Source2:        0001-PATCH-Fix-gnu-efi-crt-paths-for-Fedora.patch

BuildRequires:  binutils-devel openssl-devel pkgconfig automake libuuid-devel gnu-efi-devel >= 3.0q  help2man git

%description
Tools which can cryptographically sign EFI binaries and drivers.

%prep
%autosetup -S git_am

%build
ls /usr/lib/gnuefi /usr/lib64/gnuefi
ls
pwd
cat configure.ac
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*
%doc COPYING

%changelog
* Thu May 10 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.1-2
- build from combined source file

* Tue Feb 06 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.1-1
- bump version to 0.9.1

* Wed Jan 06 2016 Michal Sekletar <msekleta@redhat.com> - 0.6-2.gita604325
- pull in patches from Debian
- fix building release tarball

* Thu Sep 17 2015 Michal Sekletar <msekleta@redhat.com> - 0.6.1
- initial import of sbsigntools-0.6
