# TODO: webapps
Summary:	phpBugTracker is meant to be a replacement for Bugzilla
Summary(pl):	phpBugTracker - maj±cy byæ zamiennikiem dla Bugzilli
Name:		phpbt
Version:	0.9.1
Release:	1
License:	GPL (?)
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/phpbt/%{name}-%{version}.tar.gz
# Source0-md5:	5b9bc72ba1f79a78a48ddd042272f3eb
Source1:	%{name}.conf
URL:		http://phpbt.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpbtdir	%{_datadir}/%{name}

%description
phpBugTracker is meant to be a replacement for Bugzilla (one day).
It's obviously not there yet, but I'm working on it. This project grew
out of the frustrations I experienced in installing and using
bugzilla. Those frustrations inspired my design goals:

- Simplicity in use and installation
- Use templates to achieve presentation independence
- Use a database abstraction layer to achieve database independence

So this project will hopefully become a portable and powerful
web-based bug tracking solution.

%description -l pl
phpBugTracker ma byæ zamiennikiem dla Bugzilli. Jeszcze nim nie jest,
ale autor nad tym pracuje. Projekt wyrós³ z frustracji, które
prze¿ywa³ autor próbuj±c u¿ywaæ Bugzilli. Frustracje te wyznaczy³y
cele:
- prostota instalacji i u¿ywania
- u¿ywanie wzorców by uniezale¿niæ wygl±d
- u¿ywanie warstwy abstrakcji baz danych by uniezale¿niæ od konkretnej
  bazy.

Projekt ma siê staæ przeno¶nym i u¿ytecznym rozwi±zaniem ¶ledzenia
b³êdów przez WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_phpbtdir},/etc/httpd} 

cp -R * $RPM_BUILD_ROOT%{_phpbtdir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/usr/sbin/apachectl restart 1>&2
		fi
	fi
fi

%files
%defattr(644,root,root,755)
%doc docs/* CHANGELOG COPYING INSTALL README TODO UPGRADING
%dir %{_phpbtdir}
%{_phpbtdir}/*
