#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define major 5
%define oldlib5name %mklibname KF5KDcraw %{major}
%define lib5name %mklibname KF5KDcraw
%define dev5name %mklibname KF5KDcraw -d
%define libname %mklibname KDcrawQt6
%define devname %mklibname KDcrawQt6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_without qt5

Summary:	C++ interface around LibRaw library
Name:		libkdcraw
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/libkdcraw/-/archive/%{gitbranch}/libkdcraw-%{gitbranchd}.tar.bz2#/libkdcraw-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libraw)
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
%endif
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)

%rename	%{name}-common

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files
%doc README AUTHORS
%{_datadir}/qlogging-categories5/libkdcraw.categories

#----------------------------------------------------------------------
%package -n plasma6-%{name}
Summary:	C++ interface around the LibRaw library for Qt 6
Group:		System/Libraries

%description -n plasma6-%{name}

%files -n plasma6-%{name}
%{_datadir}/qlogging-categories6/libkdcraw.categories

#----------------------------------------------------------------------

%package -n %{lib5name}
Summary:	Kdcraw library
Group:		System/Libraries
Obsoletes:	%{_lib}kdcraw20 < 2:4.9.0
Obsoletes:	%{_lib}kdcraw21 < 2:4.10.0
Obsoletes:	%{_lib}kdcraw22 < 2:4.12.0
Obsoletes:	%{_lib}kdcraw23 < 2:15.12.0
Obsoletes:	%{oldlib5name} < 2:%{version}
Requires:	%{name} = %{EVRD}

%description -n %{lib5name}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{lib5name}
%{_libdir}/libKF5KDcraw.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{dev5name}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{lib5name} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90
Obsoletes:	libkdcraw-devel < 2:15.12.0

%description -n %{dev5name}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{dev5name}
%{_includedir}/KF5/KDCRAW
%{_libdir}/libKF5KDcraw.so
%{_libdir}/cmake/KF5KDcraw

#----------------------------------------------------------------------

%package -n %{libname}
Summary:	Kdcraw library for Qt 6.x
Group:		System/Libraries
Requires:	plasma6-%{name} = %{EVRD}

%description -n %{libname}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libname}
%{_libdir}/libKDcrawQt6.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name} for Qt 6.x
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KDcrawQt6
%{_libdir}/libKDcrawQt6.so
%{_libdir}/cmake/KDcrawQt6

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n libkdcraw-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=6 \
        -G Ninja

%if %{with qt5}
cd ..
export CMAKE_BUILD_DIR=build-qt5
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=5 \
        -G Ninja
%endif

%build
%ninja_build -C build
%if %{with qt5}
%ninja_build -C build-qt5
%endif

%install
%if %{with qt5}
%ninja_install -C build-qt5
%endif
%ninja_install -C build
