%global _hardened_build 1

Name:           sbsigntools
Version:        0.9.3

Release:        1%{?dist}
Summary:        EFI binary signing tools

License:        GPLv3
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/

# upsream source tarball does not contain ccan source submodule
# create combined tarball by invoking ./generate-tarball.sh $VERSION
Source0:        %{name}.combined-%{version}.tar.gz

BuildRequires:  gcc binutils-devel openssl-devel pkgconfig automake libuuid-devel gnu-efi-devel >= 3.0q  help2man git

%description
Tools which can cryptographically sign EFI binaries and drivers.

%prep
%autosetup -S git_am
./autogen.sh

%build
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
* Fri May 01 2020 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.3-1
- bump version to 0.9.3

* Thu May 09 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.2-3
- bump version to 0.9.2

* Sun Nov 11 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.1-3
- fixes for fedora 29

* Thu May 10 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.1-2
- build from combined source file

* Tue Feb 06 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.9.1-1
- bump version to 0.9.1

* Wed Jan 06 2016 Michal Sekletar <msekleta@redhat.com> - 0.6-2.gita604325
- pull in patches from Debian
- fix building release tarball

* Thu Sep 17 2015 Michal Sekletar <msekleta@redhat.com> - 0.6.1
- initial import of sbsigntools-0.6
