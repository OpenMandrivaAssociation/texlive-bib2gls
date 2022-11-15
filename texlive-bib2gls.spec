Name:		texlive-bib2gls
Version:	64945
Release:	1
Summary:	Command line application to convert .bib files to glossaries-extra.sty resource files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bib2gls
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bib2gls.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This Java command line application may be used to extract
glossary information stored in a .bib file and convert it into
glossary entry definition commands. This application should be
used with glossaries-extra.sty's 'record' package option. It
performs two functions in one: selects entries according to
records found in the .aux file (similar to bibtex),
hierarchically sorts entries and collates location lists
(similar to makeindex or xindy). The glossary entries can then
be managed in a system such as JabRef, and only the entries
that are actually required will be defined, reducing the
resources required by TeX. The supplementary application
convertgls2bib can be used to convert existing .tex files
containing definitions (\newglossaryentry etc.) to the .bib
format required by bib2gls.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/bib2gls
%{_texmfdistdir}/texmf-dist/scripts/bib2gls
%doc %{_texmfdistdir}/texmf-dist/doc/support/bib2gls
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/convertgls2bib.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/convertgls2bib.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bib2gls.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bib2gls.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
