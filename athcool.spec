# TODO: convert Japanese to EUCJP
#
Summary:	Athlon Powersaving bits enabler
Summary(ja):	AMD Athlon/Duron $B$N>JEENO5!G=$rM-8z$K$9$k(B
Summary(pl):	Narz�dzie do w��czania trybu oszcz�dno�ci energii procesor�w Athlon
Name:		athcool
Version:	0.3.0
Release:	1vl1
License:	GPL
Group:		Applications/System
URL:		http://members.jcom.home.ne.jp/jacobi/linux/softwares-ja.html
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%{name}-%{version}.tar.gz
# Source0-md5:	d41d8cd98f00b204e9800998ecf8427e
#Patch1: athcool-0.2.0-nakata1.patch
#Patch2: athcool-0.2.0-nakata2.patch
BuildPrereq:	pciutils-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}
Vendor:		Project Vine

%description
athcool is a small utility, enabling/disabling Powersaving mode for
AMD Athlon/Duron processors.

Powersaving works if your kernel support ACPI (APM not work), because
athcool only set/unset "Disconnect enable when STPGNT detected" bits
in the Northbridge of Chipset.

%description -l ja
$B!!(Bathcool $B$O(B AMD Athlon/Duron
$B$N>JEENO5!G=$rM-8z$K$7!"L5BL$JH/G.$rM^$($^$9!#(B CPU
$BMxMQN($,Dc$$;~$K$O7`E*$KH/G.$,8:$j$^$9!#(B
$B!!%A%C%W%;%C%H$K$h$C$F$O@5>o$K:nF0$7$J$$>l9g$b$"$j$^$9$N$G!">e5-(B
URL $B$r;2>H(B $B$N>e$G;HMQ$7$F$/$@$5$$!#(B
$B!!$J$*!">JEENO5!G=$K$O(B ACPI $BBP1~$N%+!<%M%k$,I,MW$G$9!#(B

%description -l pl
athcool jest ma�ym programem narz�dziwym s�u�acym do w��czania i wy��czania
trybu oszcz�dno�ci energii procesor�w AMD Athlon/Duron.

Tryb oszcz�dno�ci energii dzia�a gdy j�dro zawiera wsparcie dla ACPI (z APM
nie dzia�a), gdy� athcool jedynie ustawia/zeruje flagi bitowe "Disconnect
enable when STPGNT detected" w mostku p�nocnym chipsetu.

%prep
%setup -q
#%patch1 -p1
#%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_sbindir}
#install -m755 -s athcool $RPM_BUILD_ROOT%{_sbindir}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_sbindir}/athcool