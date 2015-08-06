%define name phpvirtualbox
%define version 5.0
%define release 1
%define rpmver   5.0
Summary: smserver rpm to install phpvirtualbox
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
URL: http://mirror.de-labrusse.fr
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
AutoReqProv: no

%description
smserver rpm to install phpvirtualbox

%changelog
* Thu Aug 06 2015 stephane de labrusse <stephdl@de-labrusse.fr> 5.0-1
- upstream upgrade 5.0-1

* Wed Apr 15 2015 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.3-1
- upstream upgrade 4.3-3

* Fri Dec 19 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.2-1
- upstream upgrade

* Sun May 18 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.1-2
-first release to sme9

* Wed Jan 15 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.1-1
- Update to phpvirtualbox 4.3.1, thanks to ian Moore 
- http://sourceforge.net/projects/phpvirtualbox

* Mon Dec 30 2013 JP Pialasse <tests@pialasse.com> 4.3.0-8.sme
- prepare rpm to import into buildsys

* Fri Dec 13 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.7
- remove the web authentication for the buildin phpvirtualbox authentication 

* Tue Nov 05 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.6
- change name to match the phpvirtualbox version
* Sat Oct 26 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.5
- add webauth to setting and "sme admin" as "phpvirtualbox admin" 
* Wed Oct 23 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.4
- Minor adjustment settings
* Sat Oct 19 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.3
- Initial release

%prep
%setup
#%patch0 -p1
%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
if [ $1 = 2 ] ; then
/bin/cp /opt/phpvirtualbox/config.php /opt/phpvirtualbox/config.php-your-backup-`date +%Y-%m-%d-%H-%M`
fi
%preun

%post



%postun
#uninstall

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

