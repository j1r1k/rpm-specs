%global debug_package %{nil}

Name:           nushell
Version:        0.10.0
Release:        1%{?dist}
Summary:        Modern shell written in Rust

License:        MIT
URL:            https://github.com/nushell/nushell
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# nushell requires rust-nightly
# * https://github.com/nushell/nushell/issues/362
BuildRequires:  cargo >= 1.39
BuildRequires:  rust >= 1.39
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)

%description
A modern, GitHub-era shell written in Rust.


%prep
%autosetup -p1
#curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal --default-toolchain nightly -y


%build
#cargo build --release --all-features


%install
cargo install --features=stable --root=%{buildroot}%{_prefix} --path=.
#cargo install --all-features --root=%{buildroot}%{_prefix} --path=.
rm -f   %{buildroot}%{_prefix}/.crates.toml \
        %{buildroot}%{_prefix}/.crates2.json


%files
%license LICENSE
%doc README.md
%{_bindir}/nu
%{_bindir}/nu_plugin*


%changelog
* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Tue Jan 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.0-1
- Update to 0.8.0

* Thu Dec 19 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-2
- Build with only Stable features

* Wed Dec 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Dec 18 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-2
- Build with all features. Thanks to Dennis Schridde.

* Sun Dec 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Wed Nov 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Fri Nov 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-2.20191106git01d6287
- Switch to system Rust 1.39

* Wed Nov 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1.20191106git01d6287
- Update to 0.5.0

* Thu Aug 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1.20190727git65ed458
- Initial package
