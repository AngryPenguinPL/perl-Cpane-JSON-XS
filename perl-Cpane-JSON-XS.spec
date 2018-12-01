%define upstream_name    Cpanel-JSON-XS
%define upstream_version 4.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Dummy module providing Cpanel::JSON::XS::Boolean
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
# Source0:    http://www.cpan.org/modules/by-module/Cpanel/%{upstream_name}-%{upstream_version}.tar.gz
Source0:    https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Pod::Text) >= 2.80.0
BuildRequires: perl-devel
# Avoid unwanted provides and dependencies
%{?perl_default_filter}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be _correct_ and its secondary goal is to be _fast_. To
reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason to
write yet another JSON module? While it seems there are many JSON modules,
none of them correctly handle all corner cases, and in most cases their
maintainers are unresponsive, gone missing, or not listening to bug reports
for other reasons.

See below for the Cpanel fork.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%__make test

%install
%make_install

%files
%doc COPYING Changes META.json META.yml MYMETA.yml README SIGNATURE XS eg
%{_mandir}/man3/*
%perl_vendorarch/*
/usr/bin/cpanel_json_xs
/usr/share/man/man1/cpanel_json_xs.1.xz
