Name:           mgitstatus
Version:        2.2
Release:        1%{?dist}
Summary:        Show uncommitted, untracked and unpushed changes for multiple Git repos

License:        MIT
URL:            https://github.com/fboender/multi-git-status
Source0:        https://github.com/fboender/multi-git-status/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       git

%description
Show uncommited, untracked and unpushed changes in multiple Git repositories. Scan for .git dirs up to DEPTH directories deep. The default is 2. If DEPTH is 0, the scan is infinitely deep.

%prep
%setup -q -n multi-git-status-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name} %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_mandir}/%{name}
gzip %{name}.1 > %{buildroot}/%{_mandir}/%{name}/%{name}.1.gz

%files
%license LICENSE.txt
%{_bindir}/*
%{_mandir}/*

%changelog
* Wed Nov 23 2022 Jiri Marsicek <jiri.marsicek@gmail.com> - 2.2-1
- Bump to version 2.2

* Tue May 17 2022 Jiri Marsicek <jiri.marsicek@gmail.com> - 2.1-1
- Bump to version 2.1

* Fri May 01 2020 Jiri Marsicek <jiri.marsicek@gmail.com> - 2.0-1
- Bump to version 2.0

* Fri Dec 06 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.0.d55c4cf
- initial import of mgitstatus-0.0.d55c4cf
