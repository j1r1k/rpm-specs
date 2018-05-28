#!/bin/sh
set -o errexit -o nounset -o pipefail

if [ ${#} != 1 ] ; then
  echo "Usage: ${0} VERSION"
  exit 1
fi

CCAN_HASH="b1f28e17227f2320d07fe052a8a48942fe17caa5"
SBST_VERSION="$1"

CCAN="ccan.git"
SBST="sbsigntools"

WORK_DIR="./sbsigntools-${SBST_VERSION}"

TARGET="./sbsigntools.combined-${SBST_VERSION}.tar.gz"

curl -sSLf "https://git.ozlabs.org/?p=ccan;a=snapshot;h=${CCAN_HASH};sf=tgz" > "$CCAN.tar.gz"
curl -sSLf "https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-${SBST_VERSION}.tar.gz" > "$SBST.tar.gz"

mkdir -p "${WORK_DIR}"

tar xfz "$SBST.tar.gz" --strip 1 -C "$WORK_DIR"

tar xfz "$CCAN.tar.gz" --strip 1 -C "$WORK_DIR/lib/ccan.git"

(
    cd "$WORK_DIR"
    patch -p1 < ../0001-PATCH-Fix-gnu-efi-crt-paths-for-Fedora.patch
    ./autogen.sh
)

tar cfz "$TARGET" "$WORK_DIR"/*

rm -rf "$WORK_DIR"
rm "$CCAN.tar.gz" "$SBST.tar.gz"
