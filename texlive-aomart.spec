%global tl_name aomart
%global tl_revision 79673
%global tl_bin_links aom-fullref:%{_texmfdistdir}/scripts/aomart/aom-fullref.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.37
Release:	%{tl_revision}.1
Summary:	Typeset articles for the Annals of Mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aomart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aomart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(aomart.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The package provides a class for typesetting articles for The Annals of
Mathematics.

