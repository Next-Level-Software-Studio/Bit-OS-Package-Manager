# Bit-OS-Package-Manager
O BPM é o gestor de pacotes principal do Bit-OS, mas que também é compatível com Gentoo Linux.

Para instalar em Gentoo Linux execute os seguintes comandos como administrador:

```
FOLDER="/h"
mkdir -p "$FOLDER"
git init "$FOLDER"
git -C "$FOLDER" remote add origin https://github.com/Next-Level-Software-Studio/Bit-OS-Package-Manager.git
git -C "$FOLDER" config core.sparseCheckout true
echo "install/*" >> "$FOLDER/.git/info/sparse-checkout"
git -C "$FOLDER" pull origin main
```