Name: idesk-icon-icex
Version: 0.0.2
Release: alt1

Summary: Icon for idesk icewm
Group: Graphical desktop/Icewm
License: GPL
Url: https://www.github.com/150balbes/idesk-icon-icewm
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Requires: idesk >= 0.7.5-alt18

Source0: .idesktop.tar.gz
Source1: .ideskrc

BuildArch: noarch
%description
Icon for idesk icewm

%prep
%build
%install
mkdir -p %buildroot%_sysconfdir/skel
tar -xzf %SOURCE0 -C %buildroot%_sysconfdir/skel
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/skel/.ideskrc

%files
%dir %_sysconfdir/skel/.idesktop
%_sysconfdir/skel/.idesktop/*
%_sysconfdir/skel/.ideskrc

%changelog
* Sun Mar 2 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.2-alt1
- new ver

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
