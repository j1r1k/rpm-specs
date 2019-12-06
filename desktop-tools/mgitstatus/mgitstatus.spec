Name:           mgitstatus
Version:        0.0.d55c4cf
Release:        1%{?dist}
Summary:        Show uncommitted, untracked and unpushed changes for multiple Git repos

License:        MIT
URL:            https://github.com/fboender/multi-git-status
Source0:        https://github.com/fboender/multi-git-status/tarball/d55c4cf7448a8c470b260c6555c448e83f740a21#/%{name}-%{version}.tar.gz

Requires:       git

%description
Show uncommited, untracked and unpushed changes in multiple Git repositories. Scan for .git dirs up to DEPTH directories deep. The default is 2. If DEPTH is 0, the scan is infinitely deep.

%prep
%setup -q -n fboender-multi-git-status-d55c4cf

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
* Tue Dec  6 2019 Jiri Marsicek <jiri.marsicek@gmail.com>
- initial import of mgitstatus-0.0.d55c4cf
