# Generated by rust2rpm 22
%bcond_without check
%define debug_package %{nil}

%global crate anda

Name:           rust-anda
Version:        0.2.1
Release:        1%?dist
Summary:        Andaman Build toolchain

License:        MIT
URL:            https://crates.io/crates/anda
Source:         https://github.com/FyraLabs/anda/archive/refs/tags/%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  anda-srpm-macros
BuildRequires:  openssl-devel
BuildRequires:  git-core
BuildRequires:  libgit2-devel
BuildRequires:  libssh2-devel

Requires:       mock
Requires:       rpm-build
Requires:       createrepo_c
Requires:       git-core
%global _description %{expand:
Andaman Build toolchain.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/anda
%{_mandir}/man1/anda*.1*
%config %{_sysconfdir}/bash_completion.d/anda.bash
%{_datadir}/zsh/site-functions/_anda
%{_datadir}/fish/completions/anda.fish

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build
cargo run --release -p xtask -- manpage
cargo run --release -p xtask -- completion

%install
%cargo_install

mkdir -p %{buildroot}%{_mandir}/man1/

# Install shell completions

COMPDIR="target/assets/completion"

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
cp -v $COMPDIR/bash/anda.bash %{buildroot}%{_sysconfdir}/bash_completion.d/anda.bash
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
cp -v $COMPDIR/zsh/_anda %{buildroot}%{_datadir}/zsh/site-functions/_anda
mkdir -p %{buildroot}%{_datadir}/fish/completions/
cp -v $COMPDIR/fish/anda.fish %{buildroot}%{_datadir}/fish/completions/anda.fish

# install man pages
cp -v target/assets/man_pages/* %{buildroot}%{_mandir}/man1/


rm -rf %{buildroot}%{cargo_registry}

%changelog
%autochangelog
