%global tl_name bib2gls
%global tl_revision 76845

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
Requires(pre):	texlive-tlpkg
Requires:	texlive(bib2gls.bin)
Requires:	texlive(glossaries-extra)
Provides:	texlive(%{tl_name}) = %{tl_revision}

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
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls
%dir %{_datadir}/texmf-dist/texmf-dist/source/support
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/resources
%dir %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bib2gls.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bib2gls.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/convertgls2bib.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/convertgls2bib.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/datatool2bib.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/datatool2bib.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/CHANGES
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/DEPENDS.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/bib2gls-begin.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/bib2gls.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/animals.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/bacteria.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/baseunits.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/bigmathsymbols.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/binaryoperators.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/books.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/chemicalformula.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/citations.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/constants.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/derivedunits.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/films.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/interpret-preamble.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/interpret-preamble2.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/markuplanguages.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/mathgreek.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/mathsobjects.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/mathsrelations.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/minerals.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/miscsymbols.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/no-interpret-preamble.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/people.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-authors.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-authors.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-bacteria.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-bacteria.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-chemical.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-chemical.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-citations.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-citations.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-constants.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-constants.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-hierarchical.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-hierarchical.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-markuplanguages.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-markuplanguages.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-maths.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-maths.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-media.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-media.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-msymbols.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-msymbols.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-multi1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-multi1.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-multi2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-multi2.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-nested.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-nested.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-people.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-people.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-textsymbols.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-textsymbols.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-textsymbols2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-textsymbols2.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units1.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units2.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units2.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units3.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-units3.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-usergroups.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/sample-usergroups.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/terms.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/topics.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/unaryoperators.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/usergroups.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/bib2gls/examples/vegetables.bib
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/bib2gls.jar
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/bib2gls.sh
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/bibglscommon.jar
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/convertgls2bib.jar
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/convertgls2bib.sh
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/datatool2bib.jar
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/datatool2bib.sh
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/resources/bib2gls-en.xml
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/resources/bib2gls-extra-en.xml
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/resources/bib2gls-extra-nl.xml
%{_datadir}/texmf-dist/texmf-dist/scripts/bib2gls/texparserlib.jar
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls-begin.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls-cite.bib
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls-src.zip
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls-terms.bib
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls.bib
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls.pod
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/bib2gls.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/convertgls2bib.pod
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/datatool2bib.pod
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/texparser-src.zip
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/bib2gls/version.tex
