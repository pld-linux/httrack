Summary:	Great website copier for offline browsing
Summary(pl):	Narzêdzie do ¶ci±gnia stron w celu przegl±dania offline
Name:		httrack
Version:	3.10
Release:	2
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.httrack.com/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.httrack.com/
BuildRequires:	perl
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

%prep
%setup -q

%build
cd src
# do not use %configure
./configure \
	--prefix=%{_prefix} \
	--etcdir=%{_sysconfdir} \
	--zlib --dynamic \
	--system=linux \
	--pthread
%{__make} CFLAGS="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_sysconfdir}}

install src/httrack $RPM_BUILD_ROOT%{_bindir}
install src/libhttrack.* $RPM_BUILD_ROOT%{_libdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nfr README *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HelpHtml httrack httrack-doc.html *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%config(noreplace) %{_sysconfdir}/httrack.conf
