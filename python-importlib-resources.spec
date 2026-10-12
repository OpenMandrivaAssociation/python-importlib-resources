Name:		python-importlib-resources
Version:	7.1.0
Release:	1
Summary:	Read resources from Python packages
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/python/importlib_resources
Source0:	https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)

%description
Backport/standalone of importlib.resources. Aider still imports this
module name.

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/importlib_resources
%{py_sitedir}/importlib_resources-*.*-info
