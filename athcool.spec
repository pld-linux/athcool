Summary:	Athlon Powersaving bits enabler
Summary(ja):	AMD Athlon/Duron の省電力機能を有効にする
Summary(pl):	Narz�dzie do w咳czania trybu oszcz�dno�ci energii procesor�w Athlon
Name:		athcool
Version:	0.3.8
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%{name}-%{version}.tar.gz
# Source0-md5:	42562a1155981e573898606e0f2534be
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://members.jcom.home.ne.jp/jacobi/linux/softwares.html
BuildRequires:	pciutils-devel
PreReq:		rc-scripts
Requires(post,postun):	/sbin/chkconfig
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
athcool is a small utility for enabling/disabling powersaving mode on
AMD Athlon/Duron processors.

Powersaving works if your kernel supports ACPI (APM doesn't work),
because athcool only sets/unsets "Disconnect enable when STPGNT
detected" bits in the northern bridge of the chipset.

%description -l ja
　athcool は AMD Athlon/Duron
の省電力機能を有効にし、無駄な発熱を抑えます。 CPU
利用率が低い時には劇的に発熱が減ります。
　チップセットによっては正常に作動しない場合もありますので、上記
URL を参照 の上で使用してください。 　なお、省電力機能には ACPI
対応のカーネルが必要です。

%description -l pl
athcool jest ma�ym programem narz�dziowym s�u娠cym do w咳czania i
wy咳czania trybu oszcz�dno�ci energii procesor�w AMD Athlon/Duron.

Tryb oszcz�dno�ci energii dzia�a, gdy j�dro zawiera wsparcie dla ACPI
(z APM nie dzia�a), gdy� athcool jedynie ustawia/zeruje flagi bitowe
"Disconnect enable when STPGNT detected" w mostku p鶻nocnym chipsetu.

%prep
%setup -q

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
%{_mandir}/man8/*
