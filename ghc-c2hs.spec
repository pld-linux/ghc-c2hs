%define		pkgname	c2hs
Summary:	A Haskell binding to the c2hs graphics library
Name:		ghc-%{pkgname}
Version:	0.28.6
Release:	2
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/packages/archive/%{pkgname}/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	fdb24350973ecdc2376576241707ff74
URL:		http://hackage.haskell.org/package/c2hs/
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-language-c >= 0.3.1.1
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/c2hs
