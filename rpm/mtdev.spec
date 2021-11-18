Name:       mtdev
Summary:    A library to transform all kernel MT events to protocol B (slotted)
Version:    1.1.6
Release:    1
License:    MIT
URL:        http://bitmath.org/code/mtdev/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  libtool

%description
mtdev - The mtdev is a stand-alone library which transforms all variants of
kernel MT events to the slotted type B protocol. The events put into mtdev
may be from any MT device, specifically type A without contact tracking,
type A with contact tracking, or type B with contact tracking. See the
kernel documentation for further details. The bulk of the mtdev code has
been out there since 2008, as part of the Multitouch X Driver. With this
package, finger tracking and seamless MT protocol handling is available
under a free license.


%package devel
Summary:    Development header files for use with mtdev
Requires:   %{name} = %{version}-%{release}

%description devel
Development header files for use with mtdev.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build

%autogen
%configure --disable-static
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libmtdev.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/mtdev-test
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_includedir}/mtdev*.h
