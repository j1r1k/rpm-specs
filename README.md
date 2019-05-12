# rpm-specs

Download sources defined in spec:
```
spectool -g *spec
```

Generate `sources` file:
```
md5sum [...FILES] > sources
```

Generate `srpm` file:
```
fedpkg --release [RELEASE] srpm
```
Where release is for example `f30`

Perform mock build:
```
fedpkg --release [RELEASE] mockbuild
```
Where release is for example `f30`

Build desktop-tool via copr:
```
copr-cli build en4aew/desktop-tools *src.rpm
```

Build system-tool via copr:
```
copr-cli build en4aew/system-tools *src.rpm
```
