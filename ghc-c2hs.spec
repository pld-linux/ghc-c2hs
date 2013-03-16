%define		pkgname	c2hs
Summary:	A Haskell binding to the c2hs graphics library
Name:		ghc-%{pkgname}
Version:	0.16.4
Release:	0.1
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	5650ffd0cc901be8ab874c58c83f253e
URL:		http://hackage.haskell.org/package/c2hs/
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-language-c < 0.4
BuildRequires:	ghc-language-c >= 0.3.1.1
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Requires:	ghc-language-c < 0.4
Requires:	ghc-language-c >= 0.3.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

%description
A Haskell binding to the c2hs graphics library.

%prep
%setup -q -n %{pkgname}-%{version}

%build
runhaskell Setup.hs configure -v2 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.hs build

%install
rm -rf $RPM_BUILD_ROOT

runhaskell Setup.hs copy --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/c2hs
