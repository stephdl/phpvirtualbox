# Note that I have translated the upstream version from X.X-X to X.X.X so that 
# the rpm release can be used if the spec file itself is updated.
%define upstreamversion 5.2-1

Name:           phpvirtualbox
Version:        5.2
Release:        1%{?dist}

Summary:        Web interface to Virtual Box
License:        GPLv3
URL:            http://sourceforge.net/projects/phpvirtualbox
Group:          Applications/Internet

#Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{upstreamversion}.zip
Source0:        https://github.com/phpvirtualbox/phpvirtualbox/archive/%{upstreamversion}.zip
Source1:        %{name}.conf

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

# Base Repo:
Requires:       httpd
Requires:       php >= 5.3.3
Requires:       mod_ssl
Requires:       php-soap
Requires:       php-gd

# Oracle Repo:
Requires:       VirtualBox-%{Version}

%description
An open source, AJAX implementation of the VirtualBox user interface written in
PHP. As a modern web interface, it allows you to access and control remote
VirtualBox instances. phpVirtualBox is designed to allow users to administer
VirtualBox in a headless environment - mirroring the VirtualBox GUI through its
web interface.


%prep
#%setup -q -n %{name}-%{upstreamversion}
mkdir %{name}-%{upstreamversion}
cd %{name}-%{upstreamversion}
unzip %{SOURCE0}
%build

    # Nothing to do

%install
    install -d -m 755 %{buildroot}%{_datadir}/%{name}
    cp -r %{name}-%{upstreamversion}/%{name}-%{upstreamversion}/* %{buildroot}%{_datadir}/%{name}
    cp %{buildroot}%{_datadir}/%{name}/config.php-example %{buildroot}%{_datadir}/%{name}/config.php

    # Link config file to location required by phpvirtualbox
    mkdir -p  %{buildroot}%{_sysconfdir}/%{name}
    ln -s  %{_datadir}/%{name}/config.php \
        %{buildroot}%{_sysconfdir}/%{name}/config.php

    # Install a default httpd config
    install -D %{SOURCE1} %{buildroot}/%{_sysconfdir}/httpd/conf.d/%{name}.conf


%clean
    rm -rf %{buildroot}

%files

    %defattr(-,root,root)
    %{_datadir}/%{name}
    %{_sysconfdir}/%{name}

    %config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
    %attr(640, root, apache) %{_datadir}/%{name}/config.php
    %config(noreplace) %{_sysconfdir}/%{name}/*

#    %doc %{_datadir}/%{name}/README.md
#    %doc %{_datadir}/%{name}/CHANGELOG.txt

#    %config(noreplace) %{_sysconfdir}/%{name}/*
#    %config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

#    # I am explicitly listing everything in the root directory so that I can
#    # make the config file have 640 permissions. 
#    %dir %{_datadir}/%{name}/css
#    %{_datadir}/%{name}/css/*
#    %dir %{_datadir}/%{name}/images
#    %{_datadir}/%{name}/images/*
#    %dir %{_datadir}/%{name}/js
#    %{_datadir}/%{name}/js/*
#    %dir %{_datadir}/%{name}/languages
#    %{_datadir}/%{name}/languages/*
#    %dir %{_datadir}/%{name}/panes
#    %{_datadir}/%{name}/panes/*
#    %dir %{_datadir}/%{name}/rdpweb
#    %{_datadir}/%{name}/rdpweb/*
#    %dir %{_datadir}/%{name}/tightvnc
#    %{_datadir}/%{name}/tightvnc/*
#    %dir %{_datadir}/%{name}/endpoints
#    %{_datadir}/%{name}/endpoints/*
#    %{_datadir}/%{name}/CHANGELOG.txt
#    %{_datadir}/%{name}/GPLv3.txt
#    %{_datadir}/%{name}/index.html
#    %{_datadir}/%{name}/LICENSE.txt
#    %{_datadir}/%{name}/README.md
#    %{_datadir}/%{name}/recovery.php-disabled

    # Can't place permissions on the symlink so it is done here
    #%attr(640, root, apache) %{_datadir}/%{name}/config.php

%changelog
* Mon Apr 21 2014 Travis Paul <Tr@visPaul.me> - 4.3.1-1
- Restructured spec file
- Updated for 4.3-1
* Tue Mar 27 2012 John Haverlack <haverje@users.sourceforge.net> - 4.1-7
- Rolling for VirtualBox 4.1-7
* Sun Aug 7 2011 Andrew Bauer <knnniggett@users.sourceforge.net> - 4.0-7
- Updated spec file to work with CentOS 6.
* Sat Apr 9 2011 John Haverlack <haverje@users.sourceforge.net> - 4.0-5
- Initial RPM build.
