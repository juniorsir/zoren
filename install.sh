#!/usr/bin/env bash
# Zoren Production Installer
# Downloads and installs the latest official Zoren compiler binary for your architecture.

set -euo pipefail

REPO="juniorsir/zoren"
VERSION="v1.0.0"

echo "=========================================================="
echo "  🔱 Installing Zoren Language Toolchain (${VERSION})"
echo "=========================================================="

# 1. Detect Operating System & Architecture
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

case "${ARCH}" in
    x86_64|amd64)
        TARGET_ARCH="x86_64"
        ;;
    aarch64|arm64)
        TARGET_ARCH="aarch64"
        ;;
    *)
        echo "❌ Error: Unsupported architecture: ${ARCH}"
        echo "Supported architectures: aarch64 (ARM64), x86_64 (AMD64)"
        exit 1
        ;;
esac

case "${OS}" in
    linux)
        TARGET_OS="linux"
        ;;
    darwin)
        TARGET_OS="macos"
        TARGET_ARCH="arm64"
        ;;
    *)
        echo "❌ Error: Unsupported operating system: ${OS}"
        echo "Supported platforms: Linux (aarch64/x86_64), macOS (arm64)"
        exit 1
        ;;
esac

TARBALL="zoren-${VERSION}-${TARGET_OS}-${TARGET_ARCH}.tar.gz"
DOWNLOAD_URL="https://github.com/${REPO}/releases/download/${VERSION}/${TARBALL}"

# 2. Determine Installation Target Directory
if [ -n "${PREFIX:-}" ] && [ -d "${PREFIX}/bin" ]; then
    INSTALL_DIR="${PREFIX}/bin"
elif [ -w "/usr/local/bin" ]; then
    INSTALL_DIR="/usr/local/bin"
elif sudo -n true 2>/dev/null; then
    INSTALL_DIR="/usr/local/bin"
    USE_SUDO="true"
else
    INSTALL_DIR="${HOME}/.local/bin"
    mkdir -p "${INSTALL_DIR}"
fi

echo "--> Target Platform: ${TARGET_OS}-${TARGET_ARCH}"
echo "--> Install Directory: ${INSTALL_DIR}"
echo "--> Downloading: ${DOWNLOAD_URL}"

# 3. Download and Extract Archive
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

curl -fsSL "${DOWNLOAD_URL}" -o "${TMP_DIR}/${TARBALL}"
tar -xzf "${TMP_DIR}/${TARBALL}" -C "${TMP_DIR}"

if [ "${USE_SUDO:-false}" = "true" ]; then
    sudo cp "${TMP_DIR}/bin/zoren" "${INSTALL_DIR}/zoren"
    sudo chmod +x "${INSTALL_DIR}/zoren"
else
    cp "${TMP_DIR}/bin/zoren" "${INSTALL_DIR}/zoren"
    chmod +x "${INSTALL_DIR}/zoren"
fi

echo ""
echo "✅ Installation completed successfully!"
echo "   Binary path: ${INSTALL_DIR}/zoren"

if ! command -v zoren >/dev/null 2>&1; then
    echo "⚠️ Note: ${INSTALL_DIR} is not currently in your PATH."
    echo "   Add it with: export PATH=\"${INSTALL_DIR}:\$PATH\""
else
    "${INSTALL_DIR}/zoren" --version
fi

echo "=========================================================="
echo "  Explore modules and guides: https://github.com/juniorsir/zoren"
echo "  Join the community: https://github.com/juniorsir/zoren/discussions"
echo "=========================================================="
