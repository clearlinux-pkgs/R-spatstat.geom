#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-spatstat.geom
Version  : 3.3.5
Release  : 38
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.geom_3.3-5.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.geom_3.3-5.tar.gz
Summary  : Geometrical Functionality of the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.geom-lib = %{version}-%{release}
Requires: R-deldir
Requires: R-polyclip
Requires: R-spatstat.data
Requires: R-spatstat.univar
Requires: R-spatstat.utils
BuildRequires : R-deldir
BuildRequires : R-polyclip
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.univar
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
on them. Data types include point patterns, windows (domains),
	     pixel images, line segment patterns, tessellations and hyperframes.
	     Capabilities include creation and manipulation of data
	     (using command line or graphical interaction),
	     plotting, geometrical operations (rotation, shift, rescale,
	     affine transformation), convex hull, discretisation and
	     pixellation, Dirichlet tessellation, Delaunay triangulation,
	     pairwise distances, nearest-neighbour distances,
	     distance transform, morphological operations
	     (erosion, dilation, closing, opening), quadrat counting,
	     geometrical measurement, geometrical covariance,
	     colour maps, calculus on spatial domains,
	     Gaussian blur, level sets of images, transects of images,
	     intersections between objects, minimum distance matching.
	     (Excludes spatial data on a network, which are supported by
	     the package 'spatstat.linnet'.)

%package lib
Summary: lib components for the R-spatstat.geom package.
Group: Libraries

%description lib
lib components for the R-spatstat.geom package.


%prep
%setup -q -n spatstat.geom
pushd ..
cp -a spatstat.geom buildavx2
popd
pushd ..
cp -a spatstat.geom buildavx512
popd
pushd ..
cp -a spatstat.geom buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740100521

%install
export SOURCE_DATE_EPOCH=1740100521
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/spatstat.geom/doc/downstream.txt
/usr/lib64/R/library/spatstat.geom/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.geom/help/AnIndex
/usr/lib64/R/library/spatstat.geom/help/aliases.rds
/usr/lib64/R/library/spatstat.geom/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.geom/help/paths.rds
/usr/lib64/R/library/spatstat.geom/help/spatstat.geom.rdb
/usr/lib64/R/library/spatstat.geom/help/spatstat.geom.rdx
/usr/lib64/R/library/spatstat.geom/html/00Index.html
/usr/lib64/R/library/spatstat.geom/html/R.css
/usr/lib64/R/library/spatstat.geom/info/packagesizes.txt
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
/usr/lib64/R/library/spatstat.geom/tests/testsR.R
/usr/lib64/R/library/spatstat.geom/tests/testsS.R
/usr/lib64/R/library/spatstat.geom/tests/testsT.R
/usr/lib64/R/library/spatstat.geom/tests/testsUtoZ.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so
/V4/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so
/VA/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so
/usr/lib64/R/library/spatstat.geom/libs/spatstat.geom.so
