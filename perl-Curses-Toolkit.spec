%define upstream_name    Curses-Toolkit
%define upstream_version 0.211

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An about dialog window
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Curses/Curses-Toolkit-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Curses)
BuildRequires:	perl(Curses::UI)
BuildRequires:	perl(English)
BuildRequires:	perl(IO::Pty::Easy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::FollowPBP)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(Moose::Meta::Attribute::Custom::Trait::Chained)
BuildRequires:	perl(POE)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Tie::Array::Iterable)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(aliased)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)

BuildArch:	noarch

%description
This module tries to be a modern curses toolkit, based on the Curses
module, to build "semi-graphical" user interfaces easily.

*WARNING* : This is still in "beta" version, not all the features are
implemented, and the API may change. However, most of the components are
there, and things should not change that much in the future... Still, don't
use it in production, and don't consider it stable.

the Curses::Toolkit manpage is meant to be used with a mainloop, which is
not part of this module. I recommend you the POE::Component::Curses
manpage, which is probably what you want. the POE::Component::Curses
manpage uses Curses::Toolkit, but provides a mainloop and handles keyboard,
mouse, timer and other events, whereas Curses::Toolkit is just the drawing
library. See the example above. the 'spawn' method returns a the
Curses::Toolkit manpage object, which you can call methods on.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.207.0-1mdv2011.0
+ Revision: 688744
- update to new version 0.207

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.206.0-2
+ Revision: 657400
- rebuild for updated spec-helper

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.206.0-1
+ Revision: 646375
- new version

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.680-1mdv2011.0
+ Revision: 517117
- update to 0.100680

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.630-1mdv2010.1
+ Revision: 514463
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.100630

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.320-1mdv2010.1
+ Revision: 510256
- import perl-Curses-Toolkit


* Tue Feb 23 2010 cpan2dist 0.100320-1mdv
- initial mdv release, generated with cpan2dist


