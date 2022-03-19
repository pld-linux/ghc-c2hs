%define		pkgname	c2hs
Summary:	A Haskell binding to the c2hs graphics library
Name:		ghc-%{pkgname}
Version:	0.28.8
Release:	2
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	0d21188ad3737724e500982b88e32b9d
URL:		http://hackage.haskell.org/package/c2hs/
BuildRequires:	ghc >= 8.0
BuildRequires:	ghc-base >= 2
BuildRequires:	ghc-bytestring
BuildRequires:	ghc-dlist
BuildRequires:	ghc-filepath
BuildRequires:	ghc-language-c >= 0.7.1
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Requires:	ghc-base >= 2
Requires:	ghc-bytestring
Requires:	ghc-dlist
Requires:	ghc-filepath
Requires:	ghc-language-c >= 0.7.1
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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/c2hs
