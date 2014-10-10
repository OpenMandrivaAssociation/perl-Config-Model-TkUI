%define upstream_name    Config-Model-TkUI
%define upstream_version 1.339

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.339
Release:    2

Summary:    GUI for conf editors based on Config::Model
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/Config-Model-TkUI-1.339.tar.gz

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
BuildRoot:  %{_tmppath}/%{name}-%{version}

Requires: perl(Config::Model)

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


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.325.0-1mdv2011.0
+ Revision: 688740
- update to new version 1.325

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.324.0-1
+ Revision: 677323
- update to new version 1.324

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.323.0-1
+ Revision: 659888
- update to new version 1.323

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.322.0-2
+ Revision: 657398
- rebuild for updated spec-helper

* Thu Mar 10 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.322.0-1
+ Revision: 643364
- new version
- remove %%check
- remove a BR on Config::Model to force build
- add a BR on Log::Log4perl
- rebuild

* Tue Nov 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.317.0-1mdv2011.0
+ Revision: 595441
- update to new version 1.317

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.309.0-1mdv2011.0
+ Revision: 569960
- update to 1.309

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.308.0-1mdv2011.0
+ Revision: 561031
- update to 1.308

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.306.0-1mdv2011.0
+ Revision: 530261
- update to 1.306

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1.305.0-1mdv2010.1
+ Revision: 529816
- adding missing buildrequires:
- update to 1.305

* Sat Mar 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.304.0-1mdv2010.1
+ Revision: 518659
- update to 1.304

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.303.0-1mdv2010.1
+ Revision: 512604
- update to 1.303

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.302.0-1mdv2010.1
+ Revision: 494931
- update to 1.302

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.301.0-1mdv2010.0
+ Revision: 432802
- update to 1.301

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.211.0-2mdv2010.0
+ Revision: 393076
- fix dependencies

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.211.0-1mdv2010.0
+ Revision: 392788
- import perl-Config-Model-TkUI


* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.0-1mdv2010.0
- initial mdv release, generated with cpan2dist


