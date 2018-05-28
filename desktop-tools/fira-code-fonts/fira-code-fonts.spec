Name:           fira-code-fonts
Version:        1.204
Release:        1%{?dist}
Summary:        Monospaced font with programming ligatures

License:        OFL1.1
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/releases/download/%{version}/FiraCode_%{version}.zip

%description
Monospaced font with programming ligatures

%prep
%autosetup -c %{name}

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/fira-code
cp -pr ttf/* %{buildroot}/%{_datadir}/fonts/fira-code

%files
%{_datadir}/fonts/*

%changelog
* Wed Feb  7 2018 Jiri Marsicek <jiri.marsicek@gmail.com>
- initial import of fira-code-fonts-1.204
