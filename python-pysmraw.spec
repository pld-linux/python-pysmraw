# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver	20201125
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcpath_ver	20180716
%define		libcsplit_ver	20120701
%define		libcthreads_ver	20160404
%define		libfcache_ver	20191109
%define		libfdata_ver	20201129
%define		libfvalue_ver	20200711
%define		libhmac_ver	20200104
%define		libuna_ver	20210801
Summary:	Python 2 bindings for libsmraw library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libsmraw
Name:		python-pysmraw
Version:	20230320
Release:	2
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libsmraw/releases
Source0:	https://github.com/libyal/libsmraw/releases/download/%{version}/libsmraw-alpha-%{version}.tar.gz
# Source0-md5:	fc6460e8d099aafe19523ae3a41df02d
URL:		https://github.com/libyal/libsmraw/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libhmac-devel >= %{libhmac_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
Requires:	libcerror >= %{libcerror_ver}
Requires:	libsmraw >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libsmraw library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libsmraw.

%prep
%setup -q -n libsmraw-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python2 module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/smraw*
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libsmraw*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmraw.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libsmraw.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[13]

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysmraw.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/pysmraw.so
