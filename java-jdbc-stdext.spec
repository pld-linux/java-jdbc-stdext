Summary:	JDBC Standart Extension
Summary(pl):	Standardowe rozszerzenie JDBC
Name:		jdbc-stdext
Version:	2.0
Release:	1
License:	Sun Microsystems, Inc. Binary Code License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jdbc2_0-stdext.jar
URL:		http://java.sun.com/products/jdbc/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JDBC Standart Extension.

%description -l pl
Standardowe rozszerzenie JDBC.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javalibdir}/*.jar
