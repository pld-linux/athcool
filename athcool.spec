Summary: Athlon Powersaving bits enabler
Summary(ja): AMD Athlon/Duron の省電力機能を有効にする
Name: athcool
Version: 0.3.0
Release: 1vl1
License: GPL
Group: Applications/System
URL: http://members.jcom.home.ne.jp/jacobi/linux/softwares-ja.html
Source: http://members.jcom.home.ne.jp/jacobi/linux/files/athcool-%{version}.tar.gz
#Patch1: athcool-0.2.0-nakata1.patch
#Patch2: athcool-0.2.0-nakata2.patch
BuildPrereq: pciutils-devel
Buildroot: %{_tmppath}/%{name}-%{version}-root
ExclusiveArch: %{ix86}
Vendor: Project Vine
Distribution: Vine Linux

%description
athcool is a small utility, enabling/disabling Powersaving mode
for AMD Athlon/Duron processors.

Powersaving works if your kernel support ACPI (APM not work),
because athcool only set/unset "Disconnect enable when STPGNT detected"
bits in the Northbridge of Chipset.

%description -l ja
　athcool は AMD Athlon/Duron の省電力機能を有効にし、無駄な発熱を抑えます。
CPU 利用率が低い時には劇的に発熱が減ります。
　チップセットによっては正常に作動しない場合もありますので、上記 URL を参照
の上で使用してください。
　なお、省電力機能には ACPI 対応のカーネルが必要です。

%prep
%setup -q
#%patch1 -p1
#%patch2 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_sbindir}
#install -m755 -s athcool $RPM_BUILD_ROOT%{_sbindir}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog
%{_sbindir}/athcool

%changelog
* Sat Jun 21 2003 yamamoto <yamamoto@yu.vinelinux.org> 0.3.0-1vl1
- update to 0.3.0 which includes patches
- remove patch1 and 2

* Thu Jun 12 2003 yamamoto <yamamoto@yu.vinelinux.org> 0.2.0-1pl_n.0.2vl2
- fix description in Japanese

* Wed Jun 11 2003 yamamoto <yamamoto@yu.vinelinux.org> 0.2.0-1pl_n.0.2vl1
- fix AMD-761 bug (patch1 by Nakata <info@nakata-jp.org>)
- refine the whole (patch2 by Nakata <info@nakata-jp.org>)

* Mon Jun  9 2003 yamamoto <yamamoto@yu.vinelinux.org> 0.2.0-1vl1
- base on 0.2.0-1ok
- add summary and description in Japanese
