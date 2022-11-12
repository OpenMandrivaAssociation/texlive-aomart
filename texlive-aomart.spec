Name:		texlive-aomart
Version:	63442
Release:	1
Summary:	Typeset articles for the Annals of Mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aomart
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a class for typesetting articles for The
Annals of Mathematics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/aomart
%{_texmfdistdir}/tex/latex/aomart
%doc %{_texmfdistdir}/doc/latex/aomart
#- source
%doc %{_texmfdistdir}/source/latex/aomart

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
