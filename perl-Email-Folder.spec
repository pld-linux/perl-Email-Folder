#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Folder
Summary:	Email::Folder - read all the messages from a folder as Email::Simple objects
Summary(pl):	Email::Folder - czytanie wiadomo¶ci z folderu jako obiektów Email::Simple
Name:		perl-Email-Folder
Version:	0.8
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5149391fbc737b00f0cae5b43a696e77
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-Email-FolderType
BuildRequires:	perl-Email-Simple
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Folder - read all the messages from a folder as Email::Simple
objects.

%description -l pl
Modu³ Email::Folder czyta wszystkie wiadomo¶ci z folderu jako obiekty
Email::Simple.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
