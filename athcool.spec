Summary:	Athlon Powersaving bits enabler
Summary(ja):	AMD Athlon/Duron ¤Î¾ÊÅÅÎÏµ¡Ç½¤òÍ­¸ú¤Ë¤¹¤ë
Summary(pl):	Narzêdzie do w³±czania trybu oszczêdno¶ci energii procesorów Athlon
Name:		athcool
Version:	0.3.0
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%{name}-%{version}.tar.gz
# Source0-md5:	a97a48071d0af234fbc788b7ee82878e
Source1:	%{name}.init
Source2:	%{name}.sysconfig
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
¡¡athcool ¤Ï AMD Athlon/Duron
¤Î¾ÊÅÅÎÏµ¡Ç½¤òÍ­¸ú¤Ë¤·¡¢ÌµÂÌ¤ÊÈ¯Ç®¤òÍÞ¤¨¤Þ¤¹¡£ CPU
ÍøÍÑÎ¨¤¬Äã¤¤»þ¤Ë¤Ï·àÅª¤ËÈ¯Ç®¤¬¸º¤ê¤Þ¤¹¡£
¡¡¥Á¥Ã¥×¥»¥Ã¥È¤Ë¤è¤Ã¤Æ¤ÏÀµ¾ï¤ËºîÆ°¤·¤Ê¤¤¾ì¹ç¤â¤¢¤ê¤Þ¤¹¤Î¤Ç¡¢¾åµ­
URL ¤ò»²¾È ¤Î¾å¤Ç»ÈÍÑ¤·¤Æ¤¯¤À¤µ¤¤¡£ ¡¡¤Ê¤ª¡¢¾ÊÅÅÎÏµ¡Ç½¤Ë¤Ï ACPI
ÂÐ±þ¤Î¥«¡¼¥Í¥ë¤¬É¬Í×¤Ç¤¹¡£

%description -l pl
athcool jest ma³ym programem narzêdziowym s³u¿±cym do w³±czania i
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
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

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
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/%{name}
