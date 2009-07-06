%define upstream_name       Config-Model-TkUI
%define upstream_version    1.211

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    GUI for conf editors based on Config::Model
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Module::Build)
BuildRequires: perl(Config::Model)
BuildRequires: perl(Tk::DirSelect)
BuildRequires: perl(Tk::ObjScanner)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Carp::Assert::More)
BuildRequires: x11-server-xvfb
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class provides a GUI for the Config::Model manpage.

With this class, the Config::Model manpage and an actual configuration
model (like the Config::Model::Xorg manpage), you get a tool to edit
configuration files (e.g. '/etc/X11/xorg.conf').

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
xvfb-run ./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*

