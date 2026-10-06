# apt-dater - terminal-based remote package update manager
#
# Authors:
#   Thomas Liske <liske@ibh.de>
#
# Copyright Holder:
#   2010-2014 (C) IBH IT-Service GmbH [https://www.ibh.de/apt-dater/]
#
# License:
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this package; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#

%global commit eb3df6923262051082df2e9377516553da9ba508
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define name apt-dater
%define version 1.0.5
%define release 0~pre%{shortcommit}+mike1%{?dist}


Name:		%{name}
Summary:	Terminal-based remote package update manager
Version:	%{version}
Release:	%{release}
URL:		https://www.ibh.de/apt-dater/
Source0: https://github.com/DE-IBH/apt-dater/archive/%{commit}/apt-dater-%{shortcommit}.tar.gz
License:	GPL
Group:		System/Management
Icon:		apt-dater.xpm
Requires:	screen
Requires:	tcl
BuildRequires:	libconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRequires:	screen
BuildRequires:	tcl-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	perl
BuildRequires:	vim-common
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
Buildroot:	%{_tmppath}/%{name}-buildroot
Vendor:		IBH IT-Service GmbH (https://www.ibh.de/)

%description

apt-dater provides an easy to use ncurses frontend for managing package updates on a large number of remote hosts using SSH.
It supports Debian-based managed hosts as well as OpenSUSE and CentOS based systems.

%prep
%setup -n apt-dater-%{commit}

%build
autoreconf -fi
%configure --prefix=%{_prefix} --libexec=%{_libexecdir}/apt-dater --disable-rpath --enable-tclfilter --enable-xmlreport --enable-autoref --enable-history --enable-clusters --enable-debug

DBXSL_DIR=$(dirname "$(rpm -ql docbook-style-xsl | grep '/manpages/docbook.xsl$' | sed 's#/docbook.xsl$##')")
make DBXSL="$DBXSL_DIR"

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/usr/share/man/man1/apt-dater-host.1

%clean
rm -rf $RPM_BUILD_ROOT
make clean

%files
%defattr(-,root,root)
%{_bindir}/apt-dater
%{_bindir}/adsh
%dir %{_libdir}/apt-dater
%{_libdir}/apt-dater/*
%doc AUTHORS COPYING ChangeLog README* TODO
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
%dir %{_mandir}/manh
%{_mandir}/manh/*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/apt-dater.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/apt-dater.mo
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/apt-dater.mo
%config %dir %{_sysconfdir}/apt-dater
%config %{_sysconfdir}/apt-dater/*
%{_datadir}/xml/schema/apt-dater/*.dtd

%changelog
* Tue Oct 06 2026 Mike Gerber <mike@mike-gerber.de> - 1.0.4-0+mike1
- Update to 1.0.4
- autoreconf
- Add build req xsltproc, docbook-style-xsl

* Thu Sep 27 2018 Mike Gerber <mike@sprachgewalt.de> - 1.0.3-4
- add build req vim-common for xxd

* Wed Mar 21 2018 Mike Gerber <mike@sprachgewalt.de> - 1.0.3-3
- Use simple "make install" to fix installing DTDs

* Sun Nov  5 2017 Mike Gerber <mike@sprachgewalt.de> - 1.0.3-2
- Add changelog
- Include dist tag
- Include /etc in build
