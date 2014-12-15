%define upstream_name    Config-Model-TkUI
%define upstream_version 1.340

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    GUI for conf editors based on Config::Model
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(Carp::Assert::More)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Module::Build)
#BuildRequires: perl(Config::Model)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Tk::DirSelect)
BuildRequires: perl(Tk::ObjScanner)
BuildRequires: perl(Test::Warn)
BuildRequires: x11-server-xvfb

BuildArch: noarch

Requires: perl(Config::Model)

%description
This class provides a GUI for the Config::Model manpage.

With this class, the Config::Model manpage and an actual configuration
model (like the Config::Model::Xorg manpage), you get a tool to edit
configuration files (e.g. '/etc/X11/xorg.conf').

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc  README
%{_mandir}/man3/*
%{perl_vendorlib}/*
