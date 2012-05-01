Summary: RAS Utilities

Name:    ras-utils
Version: 6.1
Release: 1%{?dist}
Group:   Development/Tools
License: GPLv2
Source0: mce-inject.tar.bz2
Source1: aer-inject-0.1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: x86_64 i686
BuildRequires: bison, flex

%description
This package contains both the PCIE AER Injection (aer-inject) and MCE
Injection (mce-inject) tools.  They can be used to insert software simulated
AER and MCE errors.
%prep
%setup -q -c -D -T
%setup -q -c -a 1

%build
(cd mce-inject; make)
(cd aer-inject-0.1; make)

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/sbin
install -m 700 aer-inject-0.1/aer-inject %{buildroot}/sbin/aer-inject
install -m 700 mce-inject/mce-inject %{buildroot}/sbin/mce-inject
mkdir -p %{buildroot}/%{_mandir}/man8
install -m 644 mce-inject/mce-inject.8 %{buildroot}/%{_mandir}/man8/mce-inject.8
mkdir -p %{buildroot}/%{_docdir}/aer-inject-0.1
install -m 644 aer-inject-0.1/README %{buildroot}/%{_docdir}/aer-inject-0.1/README

%clean
rm -rf %{buildroot}

%post

%files
/sbin/*
%{_mandir}/man8/*
%{_docdir}/aer-inject-0.1/README

%changelog
* Fri Jan 14 2011 Prarit Bhargava <prarit@redhat.com> 6.1.1-el6
- rpmlint cleanups
* Fri Jan 14 2011 Prarit Bhargava <prarit@redhat.com> 6.1.0
- change version to reflect RHEL release
* Fri Jul 9 2010 Prarit Bhargava <prarit@redhat.com> 6.0.0
- change version to reflect RHEL release
* Wed Jul 7 2010 Prarit Bhargava <prarit@redhat.com> 1.0.0
- initial import of aer-inject
- 0.1 from http://www.kernel.org/pub/linux/utils/pci/aer-inject/
- http://git.kernel.org/?p=utils/pci/aer-inject/aer-inject.git;a=summary
- initial import of mce-inject
- 22b6fd9d6c53de44e612f31b78b964c3a10a24a1 from
  http://git.kernel.org/?p=utils/cpu/mce/mce-inject.git;a=summary
