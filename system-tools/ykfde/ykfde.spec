Name:		ykfde
Version:	0.7.4
Release:	2c1c626%{?dist}
Summary:	opening LUKS with yubikey

License:	GPLv3+
URL:		https://github.com/ewordm-de/mkinitcpio-ykfde
Source:		https://github.com/eworm-de/mkinitcpio-ykfde/archive/2c1c626ca971741ffca2ed22d77545f6befe0632.tar.gz

BuildRequires:	libyubikey-devel ykpers-devel python-markdown iniparser-devel keyutils-libs-devel libarchive-devel cryptsetup-devel
Requires:	ykpers, systemd >= 235

%description
The Package provides the ability to open a LUKS encrypted drive
with the Yubikey in challenge response mode (HMAC-SHA1)

%global debug_package %{nil}

%prep
%setup -q -n mkinitcpio-%{name}-2c1c626ca971741ffca2ed22d77545f6befe0632

%build
make MD=markdown_py %{?_smp_mflags}

%install
make install-dracut DESTDIR=%{buildroot}

%files
%config(noreplace) %{_sysconfdir}/ykfde.conf
%{_sysconfdir}/ykfde.d/
%{_bindir}/ykfde
%{_bindir}/ykfde-cpio
%{_prefix}/lib/dracut/modules.d/90ykfde
%{_prefix}/lib/ykfde/worker
%{_prefix}/lib/systemd/system/ykfde.service
%{_prefix}/lib/systemd/system/ykfde-2f.service
%{_prefix}/lib/systemd/system/ykfde-worker.service
%{_prefix}/share/doc/ykfde/README.html
%{_prefix}/share/doc/ykfde/README.md
%{_prefix}/share/doc/ykfde/README-dracut.html
%{_prefix}/share/doc/ykfde/README-dracut.md
%{_prefix}/share/doc/ykfde/README-mkinitcpio.html
%{_prefix}/share/doc/ykfde/README-mkinitcpio.md

%changelog
* Sun May 13 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.7.4
- version 0.7.4 with GCC8 patch

* Tue Oct 03 2017 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.6.4
- bumped version to upstream

* Fri Jan 16 2015 Benjamin Pereto <benjamin.pereto@gmail.com> - 0.5.1-2
- runned rpmlint
- fixed rpmlint

* Mon Jan 12 2015 Benjamin Pereto <benjamin.pereto@gmail.com> - 0.5.1-1
- update to upstream/master
- make code more splitted up in dracut / mkinitcpio

* Sat Jan 03 2015 Benjamin Pereto <benjamin.pereto@gmail.com> - 0.5.0-1
- Update Codebase
- Added dracut module
- challenges new in ykfde-challenges.img for initramfs

* Tue Dec 16 2014 Benjamin Pereto <benjamin.pereto@gmail.com> - 0.3.5-7
- rearranged the boot file
- fixed dracut module to mount /boot/ykfde and copy the challenges
- added get-challenges.sh 

* Sun Dec 14 2014 Benjamin Pereto <benjamin.pereto@gmail.com> - 0.3.5-6
- added dracut module
- settled needed files under /boot/ykfde

