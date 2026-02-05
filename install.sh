#!/bin/bash
set -e

REPO="OMikkel/imo-utils"
INSTALL_DIR="/usr/local/bin"
BINARY_NAME="imo"

# Detect OS
detect_os() {
    case "$(uname -s)" in
        Linux*)     echo "linux";;
        Darwin*)    echo "macos";;
        CYGWIN*|MINGW*|MSYS*) echo "windows";;
        *)          echo "unknown";;
    esac
}

OS=$(detect_os)

if [ "$OS" = "unknown" ]; then
    echo "Error: Unsupported operating system"
    exit 1
fi

if [ "$OS" = "windows" ]; then
    ASSET_NAME="imo-windows.exe"
    BINARY_NAME="imo.exe"
else
    ASSET_NAME="imo-${OS}"
fi

DOWNLOAD_URL="https://github.com/${REPO}/releases/latest/download/${ASSET_NAME}"

echo "Detected OS: ${OS}"
echo "Downloading ${ASSET_NAME}..."

# Create temp directory
TMP_DIR=$(mktemp -d)
trap "rm -rf ${TMP_DIR}" EXIT

# Download binary
if command -v curl &> /dev/null; then
    curl -fsSL "${DOWNLOAD_URL}" -o "${TMP_DIR}/${BINARY_NAME}"
elif command -v wget &> /dev/null; then
    wget -q "${DOWNLOAD_URL}" -O "${TMP_DIR}/${BINARY_NAME}"
else
    echo "Error: curl or wget is required"
    exit 1
fi

# Set executable permissions (Linux/macOS)
if [ "$OS" != "windows" ]; then
    chmod +x "${TMP_DIR}/${BINARY_NAME}"
    
    # Install to system directory
    if [ -w "${INSTALL_DIR}" ]; then
        mv "${TMP_DIR}/${BINARY_NAME}" "${INSTALL_DIR}/${BINARY_NAME}"
    else
        echo "Installing to ${INSTALL_DIR} (requires sudo)..."
        sudo mv "${TMP_DIR}/${BINARY_NAME}" "${INSTALL_DIR}/${BINARY_NAME}"
    fi
    
    echo "Successfully installed ${BINARY_NAME} to ${INSTALL_DIR}"
    echo "Run 'imo' to start the CLI"
else
    # Windows: install to current directory
    mv "${TMP_DIR}/${BINARY_NAME}" "./${BINARY_NAME}"
    echo "Successfully downloaded ${BINARY_NAME} to current directory"
    echo "Run './${BINARY_NAME}' to start the CLI"
fi
