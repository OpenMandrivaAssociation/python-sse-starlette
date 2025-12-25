Name:		python-sse-starlette
Version:	3.0.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sse_starlette/sse_starlette-%{version}.tar.gz
Summary:	SSE (Server-Sent Events) plugin for Starlette
URL:		https://pypi.org/project/sse-starlette/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
SSE (Server-Sent Events) plugin for Starlette

%files
%{py_sitedir}/sse_starlette
%{py_sitedir}/sse_starlette-*.*-info
