Summary: Athlon Powersaving bits enabler
Summary(ja): AMD Athlon/Duron $B$N>JEENO5!G=$rM-8z$K$9$k(B
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
$B!!(Bathcool $B$O(B AMD Athlon/Duron $B$N>JEENO5!G=$rM-8z$K$7!"L5BL$JH/G.$rM^$($^$9!#(B
CPU $BMxMQN($,Dc$$;~$K$O7`E*$KH/G.$,8:$j$^$9!#(B
$B!!%A%C%W%;%C%H$K$h$C$F$O@5>o$K:nF0$7$J$$>l9g$b$"$j$^$9$N$G!">e5-(B URL $B$r;2>H(B
$B$N>e$G;HMQ$7$F$/$@$5$$!#(B
$B!!$J$*!">JEENO5!G=$K$O(B ACPI $BBP1~$N%+!<%M%k$,I,MW$G$9!#(B

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
