Name:       swaync
Version:    0.9.0
Release:    1%{?dist}
Summary:    Notification daemon with GTK GUI
Provides:   desktop-notification-daemon
License:    GPLv3
URL:        https://github.com/ErikReider/SwayNotificationCenter
Source0:    https://github.com/ErikReider/SwayNotificationCenter/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:    meson >= 0.51.0
BuildRequires:    vala

BuildRequires: gtk3-devel >= 3.22
BuildRequires: gtk-layer-shell-devel >= 0.1
Requires: dbus
BuildRequires: glib2-devel >= 2.50
BuildRequires: gobject-introspection-devel >= 1.68
BuildRequires: libgee-devel >= 0.20
BuildRequires: json-glib-devel >= 1.0
BuildRequires: libhandy-devel >= 1.4.0
BuildRequires: systemd-devel
BuildRequires: systemd
BuildRequires: scdoc
BuildRequires: pulseaudio-libs-devel
%{?systemd_requires}

%description
A simple notification daemon with a GTK gui for notifications and the control center

%prep
%setup -T -b 0 -q -n SwayNotificationCenter-%{version}

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_user_post swaync.service

%preun
%systemd_user_preun swaync.service

%files
%doc README.md
%{_bindir}/swaync-client
%{_bindir}/swaync
%license COPYING
%{_sysconfdir}/xdg/swaync/configSchema.json
%{_sysconfdir}/xdg/swaync/config.json
%{_sysconfdir}/xdg/swaync/style.css
%{_userunitdir}/swaync.service
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/swaync
%{_datadir}/bash-completion/completions/swaync-client
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/swaync-client.fish
%{_datadir}/fish/vendor_completions.d/swaync.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_swaync
%{_datadir}/zsh/site-functions/_swaync-client
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%{_mandir}/man1/swaync-client.1.gz
%{_mandir}/man1/swaync.1.gz
%{_mandir}/man5/swaync.5.gz

# Changelog will be empty until you make first annotated Git tag.
%changelog
* Mon Feb 27 2023 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.8.0-1
- Bump to 0.8.0

* Tue Nov 29 2022 Jiri Marsicek <jiri.marsicek@gmail.com> - 0.7.3-1
- Bump to 0.7.3

