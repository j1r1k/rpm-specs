%global commit 3415b2945e3394e12a1c15867646405826fefb74
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# https://github.com/yory8/cliphist
%global goipath         github.com/sentriz/cliphist

%gometa

%global golicenses      COPYING
%global godocs          readme.md

Name:           cliphist
Version:        0.4.0
Release:        1%{dist}
Summary:        A simple clipboard manager for Wayland

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(go.etcd.io/bbolt)

Requires:       wl-clipboard >= 2.0

%description
A clipboard history manager for wayland which can write clipboard
changes to a history file and recall history with dmenu (for example).

Both text and images are supported; clipboard is preserved
byte-for-byte; leading / trailing whitespace / no whitespace or
newlines are preserved; won't break fancy editor selections like vim
wordwise, linewise, block mode; no concept of a picker, only pipes.

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/cliphist %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%doc readme.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue May 23 2023 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.4.0-1
- Bump to 0.4.0.3415b29

* Mon Feb 27 2023 Jiri Marsicek <jiri.marsicek@gmail.com> - 0-0.3.1-df85b70
- Bump to 0.3.1.df85b70

* Mon Jun 21 2021 Bob Hepple <bob.hepple@gmail.com> - 0.20210609git6e62200.20210621git6e62200
- initial package

