Name:		texlive-aomart
Version:	1.10
Release:	1
Summary:	Typeset articles for the Annals of Mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aomart
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a class for typesetting articles for The
Annals of Mathematics.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/aomart/aomalpha.bst
%{_texmfdistdir}/bibtex/bst/aomart/aomplain.bst
%{_texmfdistdir}/tex/latex/aomart/aomart.cls
%doc %{_texmfdistdir}/doc/latex/aomart/Makefile
%doc %{_texmfdistdir}/doc/latex/aomart/README
%doc %{_texmfdistdir}/doc/latex/aomart/aomart.bib
%doc %{_texmfdistdir}/doc/latex/aomart/aomart.pdf
%doc %{_texmfdistdir}/doc/latex/aomart/aomsample.bib
%doc %{_texmfdistdir}/doc/latex/aomart/aomsample.pdf
%doc %{_texmfdistdir}/doc/latex/aomart/aomsample.tex
%doc %{_texmfdistdir}/doc/latex/aomart/aomsample1.pdf
%doc %{_texmfdistdir}/doc/latex/aomart/aomsample1.tex
%doc %{_texmfdistdir}/doc/latex/aomart/fullref.pl
#- source
%doc %{_texmfdistdir}/source/latex/aomart/aomart.dtx
%doc %{_texmfdistdir}/source/latex/aomart/aomart.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
