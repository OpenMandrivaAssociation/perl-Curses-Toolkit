%define upstream_name    Curses-Toolkit
%define upstream_version 0.206

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An about dialog window
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Curses/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Curses)
BuildRequires: perl(Curses::UI)
BuildRequires: perl(English)
BuildRequires: perl(IO::Pty::Easy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(FindBin)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::FollowPBP)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(Moose::Meta::Attribute::Custom::Trait::Chained)
BuildRequires: perl(POE)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Array::Iterable)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(overload)
BuildRequires: perl(parent)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


