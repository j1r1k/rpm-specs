%global debug_package %{nil}

Name:       git-remote-gcrypt
Version:    1.3
Release:    1%{?dist}
Summary:    GNU Privacy Guard-encrypted git remote

Group:      Development Tools
License:    GPLv3
URL:        https://git.spwhitton.name/%{name}
Source0:    https://github.com/spwhitton/%{name}/archive/%{version}.tar.gz

BuildRequires: gcc python3-docutils
Requires:   gnupg2 git-core

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
%setup -q -n %{name}-%{version}


%install
export DESTDIR="%{buildroot}"
export prefix="%{_prefix}"
./install.sh

%files
%{_bindir}/%{name}
%doc /usr/share/man/man1/%{name}.1.gz

%changelog
* Fri May 01 2020 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.3-1
- Bump to 1.3

* Thu May 09 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.2-1
- Bump to 1.2

* Mon May 28 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 1.1-1
- Import from https://github.com/spwhitton/git-remote-gcrypt and bump to 1.1
