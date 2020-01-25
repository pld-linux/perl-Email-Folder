#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Email
%define		pnam	Folder
Summary:	Email::Folder - read all the messages from a folder as Email::Simple objects
Summary(pl.UTF-8):	Email::Folder - czytanie wiadomości z folderu jako obiektów Email::Simple
Name:		perl-Email-Folder
Version:	0.855
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0058c0c066bb383103976f659fa8b301
URL:		http://search.cpan.org/dist/Email-Folder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-FolderType
BuildRequires:	perl-Email-Simple
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Folder - read all the messages from a folder as Email::Simple
objects.

%description -l pl.UTF-8
Moduł Email::Folder czyta wszystkie wiadomości z folderu jako obiekty
Email::Simple.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
