Name: idesk-icon-icex
Version: 0.0.1
Release: alt6

Summary: Icon for idesk icewm
Group: Graphical desktop/Icewm
License: GPL
Url: https://www.github.com/150balbes/idesk-icon-icewm
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Requires: idesk >= 0.7.5-alt10

Source0: icon.tar

BuildArch: noarch
%description
Icon for idesk icewm

%prep
%build
%install
mkdir -p %buildroot%_sysconfdir/idesk.d/icon
tar xf %SOURCE0 -C %buildroot%_sysconfdir/idesk.d/

%files
%dir %_sysconfdir/idesk.d/icon
%_sysconfdir/idesk.d/icon/*

%changelog
* Sun Jan 29 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt6
- add idesk-x-set , dell icex-set

* Sun Jan 24 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt5
- rename

* Sun Jan 23 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt4
- add icex-set

* Sun Jan 22 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt3
- edit install HDD

* Sun Nov 15 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt2
- init
