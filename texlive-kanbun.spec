Name:		texlive-kanbun
Version:	62026
Release:	2
Summary:	Typeset kanbun-kundoku with support for kanbun annotation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kanbun
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kanbun.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kanbun.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows users to manually input macros for elements
in a kanbun-kundoku (Han Wen Xun Du ) paragraph. More
importantly, it accepts plain text input in the "kanbun
annotation" form when used with LuaLaTeX, which allows
typesetting kanbun-kundoku paragraphs efficiently.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/kanbun
%doc %{_texmfdistdir}/doc/latex/kanbun

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
