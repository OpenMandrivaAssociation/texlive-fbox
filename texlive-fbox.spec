%global tl_name fbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.07
Release:	%{tl_revision}.1
Summary:	Extended \fbox macro from standard LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package redefines \fbox to allow an optional argument for different
frames. It can be any combination of l)eft, r)ight, t)op, and b)ottom,
for example: \fbox[lt]{foo}. Using uppercase letters or a combination of
lowercase and uppercase is also possible.

