Summary:	Athlon Powersaving bits enabler
Summary(ja.UTF-8):	AMD Athlon/Duron の省電力機能を有効にする
Summary(pl.UTF-8):	Narzędzie do włączania trybu oszczędności energii procesorów Athlon
Name:		athcool
Version:	0.3.11
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://members.jcom.home.ne.jp/jacobi/linux/files/%{name}-%{version}.tar.gz
# Source0-md5:	4f550f9aaaa68a01d1e8ae31491e5406
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://members.jcom.home.ne.jp/jacobi/linux/softwares.html
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
athcool is a small utility for enabling/disabling powersaving mode on
AMD Athlon/Duron processors.

Powersaving works if your kernel supports ACPI (APM doesn't work),
because athcool only sets/unsets "Disconnect enable when STPGNT
detected" bits in the northern bridge of the chipset.

%description -l ja.UTF-8
　athcool は AMD Athlon/Duron
の省電力機能を有効にし、無駄な発熱を抑えます。 CPU
利用率が低い時には劇的に発熱が減ります。
　チップセットによっては正常に作動しない場合もありますので、上記 URL
を参照 の上で使用してください。 　なお、省電力機能には ACPI
対応のカーネルが必要です。

%description -l pl.UTF-8
athcool jest małym programem narzędziowym służącym do włączania i
wyłączania trybu oszczędności energii procesorów AMD Athlon/Duron.

Tryb oszczędności energii działa, gdy jądro zawiera wsparcie dla ACPI
(z APM nie działa), gdyż athcool jedynie ustawia/zeruje flagi bitowe
"Disconnect enable when STPGNT detected" w mostku północnym chipsetu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LIBS="`pkg-config --libs libpci`"

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
%service athcool restart

%preun
if [ "$1" = "0" ]; then
	%service athcool stop
	/sbin/chkconfig --del athcool
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_sbindir}/athcool
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%{_mandir}/man8/*
