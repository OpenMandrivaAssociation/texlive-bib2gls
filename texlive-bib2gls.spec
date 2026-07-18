%global tl_name bib2gls
%global tl_revision 76845
%global tl_bin_links bib2gls:%{_texmfdistdir}/scripts/bib2gls/bib2gls.sh convertgls2bib:%{_texmfdistdir}/scripts/bib2gls/convertgls2bib.sh datatool2bib:%{_texmfdistdir}/scripts/bib2gls/datatool2bib.sh

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.7
Release:	%{tl_revision}.1
Summary:	Command line application to convert .bib files to glossaries-extra.sty resour...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/bib2gls
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bib2gls.bin)
Requires:	texlive(glossaries-extra)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This Java command line application may be used to extract glossary
information stored in a .bib file and convert it into glossary entry
definition commands. This application should be used with glossaries-
extra.sty's 'record' package option. It performs two functions in one:
selects entries according to records found in the .aux file (similar to
bibtex), hierarchically sorts entries and collates location lists
(similar to makeindex or xindy). The glossary entries can then be
managed in a system such as JabRef, and only the entries that are
actually required will be defined, reducing the resources required by
TeX. The supplementary application convertgls2bib can be used to convert
existing .tex files containing definitions (\newglossaryentry etc.) to
the .bib format required by bib2gls.

