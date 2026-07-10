%global tl_name aomart
%global tl_revision 76110

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.36
Release:	%{tl_revision}.1
Summary:	Typeset articles for the Annals of Mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aomart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(aomart.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a class for typesetting articles for The Annals of
Mathematics.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/aomart
%dir %{_datadir}/texmf-dist/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst/aomart
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/source/latex/aomart
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/aomart/aomalpha.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/aomart/aomplain.bst
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomart.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomart.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomfrench.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomfrench.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomsample.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomsample.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomsample.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomsample1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/aomart/aomsample1.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/aom-fullref.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/aom-fullref.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/scripts/aomart/aom-fullref.pl
%doc %{_datadir}/texmf-dist/texmf-dist/source/latex/aomart/Makefile
%doc %{_datadir}/texmf-dist/texmf-dist/source/latex/aomart/aomart.dtx
%doc %{_datadir}/texmf-dist/texmf-dist/source/latex/aomart/aomart.ins
%{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart/aom_orcid_logo.eps
%{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart/aom_orcid_logo.pdf
%{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart/aom_orcid_logo_bw.eps
%{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart/aom_orcid_logo_bw.pdf
%{_datadir}/texmf-dist/texmf-dist/tex/latex/aomart/aomart.cls
