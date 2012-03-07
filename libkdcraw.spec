Name:libkdcraw
Summary: C++ interface around LibRaw library
Version: 4.8.1
Release: 1
Epoch: 2
Group: System/Libraries
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: lcms-devel
BuildRequires: automoc4

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files
%doc README AUTHORS NEWS TODO COPYING

#----------------------------------------------------------------------

%package common
Summary: Non-library files for the kdcraw library
Group: System/Libraries

%description common
Common files for the kdcraw library

%files common
%_kde_appsdir/libkdcraw
%_kde_iconsdir/hicolor/*/apps/kdcraw.png

#------------------------------------------------	

%define	kdcraw_major 20
%define	libkdcraw %mklibname kdcraw %kdcraw_major

%package -n %{libkdcraw}
Summary: Kdcraw library
Group: System/Libraries

%description -n %{libkdcraw}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libkdcraw}
%_kde_libdir/libkdcraw.so.%{kdcraw_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: %libkdcraw = %epoch:%version-%release
Requires: lcms-devel
Conflicts: kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%_includedir/libkdcraw/
%_kde_libdir/libkdcraw.so
%_kde_libdir/pkgconfig/libkdcraw.pc

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
