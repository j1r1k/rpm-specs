Name: ponymix
Version: 5
Release: 1%{?dist}
Summary: CLI volume control for PulseAudio

License: MIT
URL: https://github.com/falconindy/%{name}
Source0: https://github.com/falconindy/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: g++ pulseaudio-libs-devel
Requires: pulseaudio
Recommends: bash-completion zsh

%description
Ponymix is a command line mixer for PulseAudio.

%prep
%setup -q

%build
%make_build

%install
%make_install


%check


%files
%license
%doc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Wed Aug 14 2019 Jiri Marsicek <jiri.marsicek@gmail.com> - 5-1
- Initial import
