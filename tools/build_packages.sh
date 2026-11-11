#!/usr/bin/env bash
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="1.0.0"
ARCH="aarch64"
DEB_ARCH="arm64"
DIST_DIR="${REPO_ROOT}/release"

echo "=================================================="
echo "Zoren Production Package Distribution Builder v${VERSION}"
echo "=================================================="
echo "Repository Root : ${REPO_ROOT}"
echo "Output Directory: ${DIST_DIR}"
echo "Architecture    : ${ARCH} (deb: ${DEB_ARCH})"
echo "=================================================="

mkdir -p "${DIST_DIR}"
WORK_DIR=$(mktemp -d -t zoren_pkg_build.XXXXXX 2>/dev/null || mktemp -d "${TMPDIR:-/data/data/com.termux/files/usr/tmp}/zoren_pkg_build.XXXXXX")
trap 'rm -rf "${WORK_DIR}"' EXIT

# 1. Verify Compiler Binaries
echo "[1/4] Checking release binaries..."
if [ ! -f "${REPO_ROOT}/bin/zoren" ]; then
    echo "Compiling zoren release binary with cargo..."
    (cd "${REPO_ROOT}/zoren" && cargo build --release)
    cp "${REPO_ROOT}/zoren/target/release/zorenv1" "${REPO_ROOT}/bin/zorenv1"
    cp "${REPO_ROOT}/zoren/target/release/zorenv1" "${REPO_ROOT}/bin/zoren"
fi

chmod +x "${REPO_ROOT}/bin/zoren" "${REPO_ROOT}/bin/zorenv1"
echo "  └── Verified binary: ${REPO_ROOT}/bin/zoren ($(du -h "${REPO_ROOT}/bin/zoren" | cut -f1))"

# 2. Build Standalone Portable Distribution Tarball (.tar.gz)
echo "[2/4] Assembling standalone distribution archive..."
TAR_STAGING="${WORK_DIR}/zoren-${VERSION}"
mkdir -p "${TAR_STAGING}/bin" "${TAR_STAGING}/std" "${TAR_STAGING}/docs" "${TAR_STAGING}/examples"

cp "${REPO_ROOT}/bin/zoren" "${TAR_STAGING}/bin/"
cp "${REPO_ROOT}/bin/zorenv1" "${TAR_STAGING}/bin/"
cp -r "${REPO_ROOT}/std/"* "${TAR_STAGING}/std/"
cp -r "${REPO_ROOT}/examples/"* "${TAR_STAGING}/examples/"
cp -r "${REPO_ROOT}/docs/"* "${TAR_STAGING}/docs/"
cp "${REPO_ROOT}/install.sh" "${TAR_STAGING}/"

TAR_OUT="${DIST_DIR}/zoren-${VERSION}-linux-${ARCH}.tar.gz"
tar -czf "${TAR_OUT}" -C "${WORK_DIR}" "zoren-${VERSION}"
echo "  └── Generated: ${TAR_OUT} ($(du -h "${TAR_OUT}" | cut -f1))"

# 3. Build Debian / Termux Package (.deb)
echo "[3/4] Building production .deb distribution package..."
DEB_STAGING="${WORK_DIR}/deb"
mkdir -p "${DEB_STAGING}/DEBIAN"
mkdir -p "${DEB_STAGING}/usr/bin"
mkdir -p "${DEB_STAGING}/usr/lib/zoren/std"
mkdir -p "${DEB_STAGING}/usr/share/doc/zoren"

cat > "${DEB_STAGING}/DEBIAN/control" <<EOF
Package: zoren
Version: ${VERSION}
Section: devel
Priority: optional
Architecture: ${DEB_ARCH}
Maintainer: Zoren Core Team <core@zoren.org>
Depends: libc6 | libc
Homepage: https://zoren.org
Description: Zoren Language Platform - High-Performance Safe Systems Programming Language
 Zoren is a systems programming language engineered for deterministic low-latency,
 zero-overhead arena allocation, and whole-program verified capabilities.
EOF

cat > "${DEB_STAGING}/DEBIAN/postinst" <<'EOF'
#!/bin/sh
set -e
echo "Zoren Language Platform v1.0.0 installed successfully."
echo "Execute 'zoren --version' to get started."
exit 0
EOF
chmod 755 "${DEB_STAGING}/DEBIAN/postinst"

cp "${REPO_ROOT}/bin/zoren" "${DEB_STAGING}/usr/bin/"
cp "${REPO_ROOT}/bin/zorenv1" "${DEB_STAGING}/usr/bin/"
chmod 755 "${DEB_STAGING}/usr/bin/zoren" "${DEB_STAGING}/usr/bin/zorenv1"
cp -r "${REPO_ROOT}/std/"* "${DEB_STAGING}/usr/lib/zoren/std/"
cp "${REPO_ROOT}/docs/README.md" "${DEB_STAGING}/usr/share/doc/zoren/"

chmod -R 755 "${DEB_STAGING}"

DEB_OUT="${DIST_DIR}/zoren_${VERSION}_${DEB_ARCH}.deb"
if command -v dpkg-deb >/dev/null 2>&1; then
    dpkg-deb --build "${DEB_STAGING}" "${DEB_OUT}"
else
    # Build standard ar-based deb package manually
    cd "${DEB_STAGING}"
    echo "2.0" > "${WORK_DIR}/debian-binary"
    (cd "${DEB_STAGING}/DEBIAN" && tar -czf "${WORK_DIR}/control.tar.gz" *)
    (cd "${DEB_STAGING}" && tar --exclude='./DEBIAN' -czf "${WORK_DIR}/data.tar.gz" usr)
    ar rcs "${DEB_OUT}" "${WORK_DIR}/debian-binary" "${WORK_DIR}/control.tar.gz" "${WORK_DIR}/data.tar.gz"
fi
echo "  └── Generated: ${DEB_OUT} ($(du -h "${DEB_OUT}" | cut -f1))"

# 4. Generate Cryptographic Checksums (SHA256)
echo "[4/4] Computing SHA-256 release checksums..."
(cd "${DIST_DIR}" && sha256sum "zoren-${VERSION}-linux-${ARCH}.tar.gz" "zoren_${VERSION}_${DEB_ARCH}.deb" > SHA256SUMS)
echo "  └── Generated: ${DIST_DIR}/SHA256SUMS"
cat "${DIST_DIR}/SHA256SUMS"

echo "=================================================="
echo "Packaging Completed Successfully!"
echo "Distribution assets ready in: ${DIST_DIR}"
echo "=================================================="
