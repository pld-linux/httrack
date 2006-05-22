Summary:	Great website copier for offline browsing
Summary(pl):	Narzêdzie do ¶ci±gania stron w celu ich przegl±dania offline
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

%description -l pl
HTTrack jest ³atwym w u¿yciu narzêdziem do przegl±dania offline.
Pozwala na ¶ci±gniêcie kopii serwera na dysk lokalny, wraz z tekstami
i obrazkami, aby móc je pó¼niej ogl±daæ przegl±dark± offline. Program
ten jest odpowiednikiem Teleporta(TM) pod Windows(TM). HTTrack
umo¿liwia równie¿ uaktualnienie wcze¶niej ¶ci±gniêtych stron,
dogrywaj±c na dysk lokalny jedynie ró¿nice pomiêdzy star± a now± ich
wersj±.

%package devel
Summary:	HTTtack header files
Summary(pl):	Pliki nag³ówkowe HTTrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for developing applications that use HTTrack.

%description devel -l pl
Pliki nag³ówkowe konieczne do rozwoju aplikacji u¿ywaj±cych HTTrack.

%package static
Summary:	Static httrack library
Summary(pl):	Statyczna biblioteka httrack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static httrack library.

%description static -l pl
Statyczna biblioteka httrack.

%package web
Summary:	Web frontend server to httrack
Summary(pl):	Graficzny interfejs do httrack przez przegl±darkê WWW
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description web
This package is a web frontend server to httrack.

%description web -l pl
Graficzny interfejs do httrack przez przegl±darkê WWW.

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
%{_desktopdir}/*
