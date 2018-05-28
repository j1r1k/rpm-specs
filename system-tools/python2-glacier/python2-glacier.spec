Name:           python2-glacier
Version:        0.0.1
Release:        8982862%{?dist}
Summary:        Command-line interface to Amazon Glacier

License:        MIT
URL:            https://github.com/basak/glacier-cli
Source0:        https://github.com/basak/glacier-cli/tarball/89828628694367b54f6c9b418c4de0ba6b3f5362

Patch0:         0001-change-shebang-to-python2.patch

BuildArch:      noarch
Requires:       python2-boto python2-iso8601 python2-sqlalchemy

%description
Command-line interface to Amazon Glacier

%prep
%setup -q -n basak-glacier-cli-8982862

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 glacier.py %{buildroot}%{_bindir}/glacier

%files
%license COPYING
%doc README.md
%{_bindir}/glacier

%changelog
* Sat May 26 2018 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.0.8982862-1
- import python2-glacier 8982862
