#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-overdue
Version  : 1
Release  : 1
URL      : https://github.com/clearlinux/swupd-overdue/releases/download/v1/swupd-overdue-1.tar.xz
Source0  : https://github.com/clearlinux/swupd-overdue/releases/download/v1/swupd-overdue-1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: swupd-overdue-bin
Requires: swupd-overdue-config
Requires: swupd-overdue-doc
BuildRequires : pkgconfig(systemd)

%description
No detailed description available

%package bin
Summary: bin components for the swupd-overdue package.
Group: Binaries
Requires: swupd-overdue-config

%description bin
bin components for the swupd-overdue package.


%package config
Summary: config components for the swupd-overdue package.
Group: Default

%description config
config components for the swupd-overdue package.


%package doc
Summary: doc components for the swupd-overdue package.
Group: Documentation

%description doc
doc components for the swupd-overdue package.


%prep
%setup -q -n swupd-overdue-1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../swupd-overdue.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-overdue.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd-overdue

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-overdue.service
/usr/lib/systemd/system/swupd-overdue.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
