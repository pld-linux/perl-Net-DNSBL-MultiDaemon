# TODO
# - daemon package
#
# Conditional build:
%bcond_with	tests		# perform "make test" (uses DNS servers)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNSBL-MultiDaemon
Summary:	Net::DNSBL::MultiDaemon - multi DNSBL prioritization
Summary(pl):	Net::DNSBL::MultiDaemon - obs³uga wielu DNSBL z priorytetami
Name:		perl-Net-DNSBL-MultiDaemon
Version:	0.18
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIKER/Net-DNSBL-MultiDaemon-%{version}.tar.gz
# Source0-md5:	7822d4c33316b164773d3c3f6d351cd4
URL:		http://search.cpan.org/dist/Net-DNSBL-MultiDaemon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Geo-IP-PurePerl >= 1.1
BuildRequires:	perl-Net-DNS-Codes >= 0.08
BuildRequires:	perl-Net-DNS-ToolKit >= 0.24
BuildRequires:	perl-NetAddr-IP-Lite >= 0.02
BuildRequires:	perl-Unix-Syslog >= 0.97
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DNSBL::MultiDaemon is the Perl module that implements the
multi_dnsbl daemon.

multi_dnsbl is a DNS emulator daemon that increases the efficacy of
DNSBL look-ups in a mail system. multi_dnsbl may be used as a
stand-alone DNSBL or as a plug-in for a standard BIND 9 installation.
multi_dnsbl shares a common configuration file format with the
Mail::SpamCannibal sc_BLcheck.pl script so that DNSBL's can be
maintained in a common configuration file for an entire mail
installation.

%description -l pl
Net::DNSBL::MultiDaemon to modu³ Perla implementujacy demona
multi_dnsbl.

multi_dnsbl to demon emuluj±cy DNS zwiêkszaj±cy wydajno¶æ wyszukiwañ
DNSBL w systemach pocztowych. multi_dnsbl mo¿e byæ u¿ywany jako
samodzielny DNSBL lub jako wtyczka dla standardowej instalacji BIND-a
9. multi_dnsbl wspó³dzieli format pliku konfiguracyjnego ze skryptem
sc_BLcheck.pl z pakietu Mail::SpamCannibal, wiêc DNSBL-e mog± byæ
zarz±dzane z poziomu tego samego pliku konfiguracyjnego, co ca³y
system pocztowy.

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
%doc Changes multi_dnsbl.conf.sample scripts/list_countries.pl rc.multi_dnsbl
%dir %{perl_vendorlib}/Net/DNSBL
%{perl_vendorlib}/Net/DNSBL/*.pm
%dir %{perl_vendorlib}/auto/Net/DNSBL
%dir %{perl_vendorlib}/auto/Net/DNSBL/Utilities
%{perl_vendorlib}/auto/Net/DNSBL/Utilities/autosplit.ix
%{perl_vendorlib}/auto/Net/DNSBL/Utilities/*.al
%{_mandir}/man3/*
