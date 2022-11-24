Name: diff-so-fancy
Version: 1.4.2
Release: 4%{?dist}
Summary: Good-lookin' diffs. Actually… nah… The best-lookin' diffs.

License: MIT	
URL: https://github.com/so-fancy/diff-so-fancy
Source0: https://github.com/so-fancy/diff-so-fancy/archive/refs/tags/v%{version}.tar.gz

%description
diff-so-fancy strives to make your diffs human readable instead of machine readable. This helps improve code quality and helps you spot defects faster.

%global debug_package %{nil}

%prep
%setup -q

%build
sed -i -e 's|use lib.*|use lib "%{_datadir}/%{name}/lib";|' diff-so-fancy

%install
install -vdm 0755 %{buildroot}%{_bindir}
install -vdm 0755 %{buildroot}%{_datadir}/%{name}
install -vdm 0755 %{buildroot}%{_datadir}/%{name}/lib
install -Dpm 0644 lib/DiffHighlight.pm %{buildroot}%{_datadir}/%{name}/lib/
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/lib/DiffHighlight.pm

%changelog
* Wed Feb 23 2022 Antoni Segura Puimedon <antoni@redhat.com> 1.4.2-4
- Do not use git annex for the source (antoni@redhat.com)

* Wed Feb 23 2022 Antoni Segura Puimedon <antoni@redhat.com> 1.4.2-3
- Use notgz tito builder (antoni@redhat.com)

* Wed Feb 23 2022 Antoni Segura Puimedon <antoni@redhat.com>
- Use notgz tito builder (antoni@redhat.com)

* Wed Feb 23 2022 Antoni Segura Puimedon <antoni@redhat.com> 1.4.2-2
- Set copr releaser (antoni@redhat.com)

* Fri Jun 18 2021 Antoni Segura Puimedon <antoni@redhat.com> 1.4.2-1
- Add copr repo readme (antoni@redhat.com)
- tito fixes (antoni@redhat.com)

* Fri Jun 18 2021 Antoni Segura Puimedon <antoni@redhat.com> 1.4.2-0
- Update to v1.4.2 package with tito

* Wed Apr 29 2020 Antoni Segura Puimedon <toni@sepu.cz> 1.3.0-1
- Initial package
