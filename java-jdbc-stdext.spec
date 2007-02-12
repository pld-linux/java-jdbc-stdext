Summary:	JDBC Standart Extension
Summary(pl.UTF-8):   Standardowe rozszerzenie JDBC
Name:		jdbc-stdext
Version:	2.0
Release:	2
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
Source0:	jdbc2_0-stdext.jar
URL:		http://java.sun.com/products/jdbc/
NoSource:	0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
JDBC 2.0 Standard Extension.

%description -l pl.UTF-8
Standardowe rozszerzenie JDBC 2.0.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_javalibdir}
ln -sf jdbc2_0-stdext.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javalibdir}/*.jar
