#
# spec file for package rofi-calc
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           rofi-calc
Version:        2.1.0
Release:        1.7
Summary:        Calculator for rofi
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/svenstaro/rofi-calc
Source0:        https://github.com/svenstaro/rofi-calc/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  rofi >= 1.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(rofi) >= 1.5
Requires:       qalculate >= 2.0
Requires:       rofi >= 1.5

%description
A rofi plugin that uses libqalculate's qalc to parse natural language
input and provide results.

Since this uses libqalculate's qalc, natural language queries such as
"500 + 25%%" or "5000 EUR to USD" or "150 to hex" can be input.
It can also solve linear equations on the fly, like "60x + 30 = 50"
for instance.

%prep
%setup -q

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/rofi/calc.la

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/rofi
%{_libdir}/rofi/calc.so

%changelog
* Tue May 17 2022 Jiri Marsicek <jiri.marsicek@gmail.com> - 2.1.0-1.7
- Update to 2.1.0
* Mon Nov 16 2020 Michael Vetter <mvetter@suse.com>
- Update to 2.0.0:
  * Add option to completely disable history #63
* Thu Sep 24 2020 Michael Vetter <mvetter@suse.com>
- Update to 1.9:
  * Add options to specify output hints (#59)
* Thu Aug 13 2020 Michael Vetter <mvetter@suse.com>
- Update to 1.8:
  * Enable qalc's Unicode mode by default
  * Add -no-unicode option to disable aforementioned unicode support
* Mon May  4 2020 Michael Vetter <mvetter@suse.com>
- Update to 1.7:
  * Fix file descriptor leak (#42)
  * Add a note about saving the result to clipboard (#43)
  * Document how to change decimal separator (#44)
  * Use echo -n for clipboard
* Fri Jan 24 2020 Michael Vetter <mvetter@suse.com>
- Update to 1.6:
  * Add option -qalc-binary to specify the name or path to the qalc binary
  * Document comma & space seperator options in README
  * Delete items from history file (#34)
  * Added version check in configure.ac (#28)
* Wed Apr 24 2019 mvetter@suse.com
- Update to 1.5:
  * Fix invalid free in case rofi dir didn't already exist
* Tue Apr 23 2019 mvetter@suse.com
- Update to 1.4:
  * Fix parsing result with -terse
  * Add history feature (#6)
* Tue Apr  2 2019 mvetter@suse.com
- Update to 1.3:
  * Add -no-bold flag to disable bold results
  * Implement -terse option
* Mon Apr  1 2019 mvetter@suse.com
- Update to 1.1:
  * Add -calc-command to specify a shell command (#3)
  * Execute with last_result from qalc when Ctrl+Enter is pressed (#3)
* Thu Mar 14 2019 Jan Engelhardt <jengelh@inai.de>
- Encode %% inside description. Trim bias from description.
* Wed Mar 13 2019 mvetter@suse.com
- Update to 1.0:
  * Better dependency form
  * Check for cairo
  * Add qalculate version warning
  * Use pluginsdir for installation
  * Do not hardcode rofi path
* Wed Mar 13 2019 mvetter@suse.com
- Import 0.1+20180729.f24ac5e from home:siegel
