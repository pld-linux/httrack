Summary:	Great website copier for offline browsing
Summary(pl.UTF-8):	Narzędzie do ściągania stron w celu ich przeglądania offline
Name:		httrack
Version:	3.40
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.httrack.com/%{name}-%{version}.tar.gz
# Source0-md5:	0364c56ab1e5289935d4d3482d1b82cb
Source1:	%{name}.conf
Patch0:		%{name}-desktop.patch
URL:		http://www.httrack.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTrack is an easy-to-use offline browser utility. It allows you to
download a World Wide website from the Internet to a local directory,
building recursively all directories, getting html, images, and other
files from the server to your computer. HTTrack arranges the original
site's relative link-structure. Simply open a page of the "mirrored"
website in your browser, and you can browse the site from link to
link, as if you were viewing it online. HTTrack can also update an
existing mirrored site, and resume interrupted downloads. HTTrack is
fully configurable.

%description -l pl.UTF-8
HTTrack jest łatwym w użyciu narzędziem do przeglądania offline.
Pozwala na ściągnięcie kopii serwera na dysk lokalny, wraz z tekstami
i obrazkami, aby móc je później oglądać przeglądarką offline. Program
ten jest odpowiednikiem Teleporta(TM) pod Windows(TM). HTTrack
umożliwia również uaktualnienie wcześniej ściągniętych stron,
dogrywając na dysk lokalny jedynie różnice pomiędzy starą a nową ich
wersją.

%package devel
Summary:	HTTtack header files
Summary(pl.UTF-8):	Pliki nagłówkowe HTTrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for developing applications that use HTTrack.

%description devel -l pl.UTF-8
Pliki nagłówkowe konieczne do rozwoju aplikacji używających HTTrack.

%package static
Summary:	Static httrack library
Summary(pl.UTF-8):	Statyczna biblioteka httrack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static httrack library.

%description static -l pl.UTF-8
Statyczna biblioteka httrack.

%package web
Summary:	Web frontend server to httrack
Summary(pl.UTF-8):	Graficzny interfejs do httrack przez przeglądarkę WWW
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description web
This package is a web frontend server to httrack.

%description web -l pl.UTF-8
Graficzny interfejs do httrack przez przeglądarkę WWW.

%prep
%setup -q -n %{name}-%{version}.3
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

rm -f {html,libtest,templates}/Makefile*
rm -f $RPM_BUILD_ROOT%{_libdir}/httrack/lib*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/html
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/httrack/history.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/httrack/httrack-doc.html $RPM_BUILD_ROOT%{_datadir}/%{name}/
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/html
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/httrack/html $RPM_BUILD_ROOT%{_datadir}/%{name}/html


%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc templates README greetings.txt history.txt httrack-doc.html
%doc html/images html/img html/div html/*.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httrack.conf
%attr(755,root,root) %{_bindir}/httrack
%attr(755,root,root) %{_bindir}/proxytrack
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/httrack
%attr(755,root,root) %{_libdir}/httrack/lib*.so*
%{_mandir}/man1/httrack.1*
%{_mandir}/man1/proxytrack.1*


%files devel
%defattr(644,root,root,755)
%doc libtest
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/httrack

%files static
%defattr(644,root,root,755)
%{_libdir}/libhttrack.a

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/webhttrack
%attr(755,root,root) %{_bindir}/htsserver
%{_datadir}/%{name}
%{_mandir}/man1/htsserver.1*
%{_mandir}/man1/webhttrack.1*
%{_pixmapsdir}/%{name}.xpm
%{_desktopdir}/*.desktop
