#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-overdue
Version  : 6
Release  : 12
URL      : https://github.com/clearlinux/swupd-overdue/releases/download/v6/swupd-overdue-6.tar.xz
Source0  : https://github.com/clearlinux/swupd-overdue/releases/download/v6/swupd-overdue-6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: swupd-overdue-autostart = %{version}-%{release}
Requires: swupd-overdue-bin = %{version}-%{release}
Requires: swupd-overdue-license = %{version}-%{release}
Requires: swupd-overdue-man = %{version}-%{release}
Requires: swupd-overdue-services = %{version}-%{release}
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
Patch1: run-as-nice.patch

%description
No detailed description available

%package autostart
Summary: autostart components for the swupd-overdue package.
Group: Default

%description autostart
autostart components for the swupd-overdue package.


%package bin
Summary: bin components for the swupd-overdue package.
Group: Binaries
Requires: swupd-overdue-license = %{version}-%{release}
Requires: swupd-overdue-services = %{version}-%{release}

%description bin
bin components for the swupd-overdue package.


%package license
Summary: license components for the swupd-overdue package.
Group: Default

%description license
license components for the swupd-overdue package.


%package man
Summary: man components for the swupd-overdue package.
Group: Default

%description man
man components for the swupd-overdue package.


%package services
Summary: services components for the swupd-overdue package.
Group: Systemd services

%description services
services components for the swupd-overdue package.


%prep
%setup -q -n swupd-overdue-6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555000469
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1555000469
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/swupd-overdue
cp COPYING %{buildroot}/usr/share/package-licenses/swupd-overdue/COPYING
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../swupd-overdue.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-overdue.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-overdue.service

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd-overdue

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swupd-overdue/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swupd-overdue.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-overdue.service
/usr/lib/systemd/system/swupd-overdue.service
