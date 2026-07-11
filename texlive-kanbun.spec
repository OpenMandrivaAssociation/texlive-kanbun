%global tl_name kanbun
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Typeset kanbun-kundoku with support for kanbun annotation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kanbun
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kanbun.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kanbun.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows users to manually input macros for elements in a
kanbun-kundoku (Han Wen Xun Du ) paragraph. More importantly, it accepts
plain text input in the "kanbun annotation" form when used with
LuaLaTeX, which allows typesetting kanbun-kundoku paragraphs
efficiently.

