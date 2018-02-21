# Do stuff that require Internet connection. Useful for debugging, useless in Koji.
# invoke mock with: --enable-network --with internet
%bcond_with internet


Name:           python-jupyterlab
Version:        0.31.8
Release:        1%{?dist}
Summary:        The JupyterLab notebook server extension

License:        BSD
URL:            http://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/j/jupyterlab/jupyterlab-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(ipython-genutils)
BuildRequires:  python3dist(jupyterlab-launcher) < 0.11.0
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(notebook) >= 4.3.1
BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-check-links) not available and doesn't work without interwebz
BuildRequires:  python3dist(recommonmark)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(selenium)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  %{_bindir}/node
BuildRequires:  %{_bindir}/npm

%?python_enable_dependency_generator

%description
...

%package -n     python3-jupyterlab
Summary:        %{summary}
%{?python_provide:%python_provide python3-jupyterlab}
 

%description -n python3-jupyterlab
...


%prep
%autosetup -n jupyterlab-%{version}

%build
%if %{without internet}
%global py_setup_args --skip-npm
%endif
%py3_build

# no docs in tarball yet
# generate html docs
# sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
# rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} -m pytest -vv

%files -n python3-jupyterlab
%license LICENSE
%doc README.md
%{_bindir}/jlpm
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%{_bindir}/jupyter-labhub
%{python3_sitelib}/jupyterlab
%{python3_sitelib}/jupyterlab-%{version}-py?.?.egg-info

%changelog
* Tue Feb 20 2018 Miro Hrončok <mhroncok@redhat.com> - 0.31.8-1
- Initial package
