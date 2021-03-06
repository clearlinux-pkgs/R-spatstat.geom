#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.geom
Version  : 1.65.5
Release  : 2
URL      : https://cran.r-project.org/src/contrib/spatstat.geom_1.65-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.geom_1.65-5.tar.gz
Summary  : Geometrical Functionality of the 'spatstat' Package
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.geom-lib = %{version}-%{release}
Requires: R-deldir
Requires: R-polyclip
Requires: R-spatstat.data
Requires: R-spatstat.sparse
Requires: R-spatstat.utils
BuildRequires : R-deldir
BuildRequires : R-polyclip
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.sparse
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
containing the user-level code from 'spatstat'
	     which performs geometrical operations, except for the
	     geometry of linear networks.

%package lib
Summary: lib components for the R-spatstat.geom package.
Group: Libraries

%description lib
lib components for the R-spatstat.geom package.


%prep
%setup -q -c -n spatstat.geom
cd %{_builddir}/spatstat.geom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611788248

%install
export SOURCE_DATE_EPOCH=1611788248
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.geom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.geom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.geom
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spatstat.geom || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.geom/CITATION
/usr/lib64/R/library/spatstat.geom/DESCRIPTION
/usr/lib64/R/library/spatstat.geom/INDEX
/usr/lib64/R/library/spatstat.geom/Meta/Rd.rds
/usr/lib64/R/library/spatstat.geom/Meta/features.rds
/usr/lib64/R/library/spatstat.geom/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.geom/Meta/links.rds
/usr/lib64/R/library/spatstat.geom/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.geom/Meta/package.rds
/usr/lib64/R/library/spatstat.geom/NAMESPACE
/usr/lib64/R/library/spatstat.geom/NEWS
/usr/lib64/R/library/spatstat.geom/R/spatstat.geom
/usr/lib64/R/library/spatstat.geom/R/spatstat.geom.rdb
/usr/lib64/R/library/spatstat.geom/R/spatstat.geom.rdx
/usr/lib64/R/library/spatstat.geom/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.geom/help/AnIndex
/usr/lib64/R/library/spatstat.geom/help/aliases.rds
/usr/lib64/R/library/spatstat.geom/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.geom/help/paths.rds
/usr/lib64/R/library/spatstat.geom/help/spatstat.geom.rdb
/usr/lib64/R/library/spatstat.geom/help/spatstat.geom.rdx
/usr/lib64/R/library/spatstat.geom/html/00Index.html
/usr/lib64/R/library/spatstat.geom/html/R.css
/usr/lib64/R/library/spatstat.geom/ratfor/Makefile
/usr/lib64/R/library/spatstat.geom/ratfor/dppll.r
/usr/lib64/R/library/spatstat.geom/ratfor/inxypOld.r
/usr/lib64/R/library/spatstat.geom/tests/badwindow.txt
/usr/lib64/R/library/spatstat.geom/tests/selfcross.txt
/usr/lib64/R/library/spatstat.geom/tests/testsAtoC.R
/usr/lib64/R/library/spatstat.geom/tests/testsD.R
/usr/lib64/R/library/spatstat.geom/tests/testsEtoF.R
/usr/lib64/R/library/spatstat.geom/tests/testsGtoJ.R
/usr/lib64/R/library/spatstat.geom/tests/testsK.R
/usr/lib64/R/library/spatstat.geom/tests/testsL.R
/usr/lib64/R/library/spatstat.geom/tests/testsM.R
/usr/lib64/R/library/spatstat.geom/tests/testsNtoO.R
/usr/lib64/R/library/spatstat.geom/tests/testsP1.R
/usr/lib64/R/library/spatstat.geom/tests/testsP2.R
/usr/lib64/R/library/spatstat.geom/tests/testsQ.R
/usr/lib64/R/library/spatstat.geom/tests/testsS.R
/usr/lib64/R/library/spatstat.geom/tests/testsT.R
/usr/lib64/R/library/spatstat.geom/tests/testsUtoZ.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so
/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so.avx2
/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so.avx512
