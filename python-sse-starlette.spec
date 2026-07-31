%define module sse-starlette
%define oname sse_starlette

Name:		python-sse-starlette
Version:	3.4.6
Release:	1
Summary:	SSE (Server-Sent Events) plugin for Starlette
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/sse-starlette
Source0:	https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
SSE (Server-Sent Events) plugin for Starlette

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
