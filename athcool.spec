Summary:	Athlon Powersaving bits enabler
Summary(ja):	AMD Athlon/Duron �ξ����ϵ�ǽ��ͭ���ˤ���
Summary(pl):	Narz�dzie do w��czania trybu oszcz�dno�ci energii procesor�w Athlon
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
��athcool �� AMD Athlon/Duron
�ξ����ϵ�ǽ��ͭ���ˤ���̵�̤�ȯǮ���ޤ��ޤ��� CPU
����Ψ���㤤���ˤϷ�Ū��ȯǮ������ޤ���
�����åץ��åȤˤ�äƤ�����˺�ư���ʤ����⤢��ޤ��Τǡ��嵭
URL �򻲾� �ξ�ǻ��Ѥ��Ƥ��������� ���ʤ��������ϵ�ǽ�ˤ� ACPI
�б��Υ����ͥ뤬ɬ�פǤ���

%description -l pl
athcool jest ma�ym programem narz�dziowym s�u��cym do w��czania i
wy��czania trybu oszcz�dno�ci energii procesor�w AMD Athlon/Duron.

Tryb oszcz�dno�ci energii dzia�a gdy j�dro zawiera wsparcie dla ACPI
(z APM nie dzia�a), gdy� athcool jedynie ustawia/zeruje flagi bitowe
"Disconnect enable when STPGNT detected" w mostku p�nocnym chipsetu.

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
