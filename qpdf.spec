Summary:	Content-Preserving PDF Transformation System
Name:		qpdf
Version:	5.1.2
Release:	1
License:	Artistic-2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/qpdf/%{name}-%{version}.tar.gz
# Source0-md5:	0bd15ef5eea5f628951ab456c84e78ec
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QPDF is a command-line program that does structural,
content-preserving transformations on PDF files. It could have been
called something like pdf-to-pdf. It also provides many useful
capabilities to developers of PDF-producing software or for people who
just want to look at the innards of a PDF file to learn more about how
they work.

%package devel
Summary:	Header files for qpdf library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for qpdf library.

%prep
%setup -q

%build
export CONFIG_SHELL=/bin/bash
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%check
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/qpdf
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Artistic-2.0 ChangeLog README TODO
%attr(755,root,root) %{_bindir}/fix-qdf
%attr(755,root,root) %{_bindir}/qpdf
%attr(755,root,root) %{_bindir}/zlib-flate
%attr(755,root,root) %ghost %{_libdir}/libqpdf.so.13
%attr(755,root,root) %{_libdir}/libqpdf.so.*.*.*
%{_mandir}/man1/*1.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpdf.so
%{_includedir}/qpdf
%{_pkgconfigdir}/*.pc

