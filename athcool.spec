# TODO:
# - convert Japanese to EUCJP
# - make init-script (?)
#
Summary:	Athlon Powersaving bits enabler
Summary(ja):	AMD Athlon/Duron $B$N>JEENO5!G=$rM-8z$K$9$k(B
Summary(pl):	Narzêdzie do w³±czania trybu oszczêdno¶ci energii procesorów Athlon
Name:		athcool
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%{name}-%{version}.tar.gz
# Source0-md5:	a97a48071d0af234fbc788b7ee82878e
Source1:	%{name}.init
Patch0:		%{name}-DESTDIR.patch
URL:		http://members.jcom.home.ne.jp/jacobi/linux/softwares-ja.html
BuildRequires:	pciutils-devel
PreReq:		rc-scripts
Requires(post,postun):	/sbin/chkconfig
ExclusiveArch:	%{ix86}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
athcool jest ma³ym programem narzêdziwym s³u¿acym do w³±czania i
wy³±czania trybu oszczêdno¶ci energii procesorów AMD Athlon/Duron.

Tryb oszczêdno¶ci energii dzia³a gdy j±dro zawiera wsparcie dla ACPI
(z APM nie dzia³a), gdy¿ athcool jedynie ustawia/zeruje flagi bitowe
"Disconnect enable when STPGNT detected" w mostku pó³nocnym chipsetu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add athcool

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del athcool
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_sbindir}/athcool
%attr(755,root,root) /etc/rc.d/init.d/%{name}
