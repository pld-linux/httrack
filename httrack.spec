Summary:	Great website copier for offline browsing
Name:		httrack
Version:	3.10
Release:	1
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
License:	GPL
Source0:	http://www.httrack.com/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.httrack.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	perl
BuildRequires:	zlib-devel

%description
HTTrack is an easy-to-use offline browser utility. It allows you to
download a World Wide website from the Internet to a local directory,
building recursively all directories, getting html, images, and other
files from the server to your computer. HTTrack arranges the original
site's relative link-structure.Simply open a page of the "mirrored"
website in your browser, and you can browse the site from link to
link, as if you were viewing it online. HTTrack can also update an
existing mirrored site, and resume interrupted downloads. HTTrack is
fully configurable.

%prep
%__rm -rf $RPM_BUILD_ROOT

%setup -q
touch `find . -type f`

%build
cd src

./configure --prefix=%{_prefix} --etcdir=%{_sysconfdir} --zlib --dynamic --system=linux --pthread
%{__make} CFLAGS="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_sysconfdir}}
install src/httrack $RPM_BUILD_ROOT%{_bindir}
install src/libhttrack.* $RPM_BUILD_ROOT%{_libdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nfr COPYING INSTALL README *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HelpHtml httrack httrack-doc.html *.gz
%attr (0755,root,root) %_bindir/*
%attr (0755,root,root) %_libdir/*
%attr (0644,root,root) %config (noreplace) %{_sysconfdir}/httrack.conf
