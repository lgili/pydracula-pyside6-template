import os
# Constroi o Flatpak
os.system('flatpak-builder build _packaging/flatpak/com.lgili.pydracula.yaml --force-clean --ccache')
# Exporta o resultado para a pasta export
os.system('flatpak build-export export build')
# Cria o arquivo único
os.system('flatpak build-bundle export export/pydracula.flatpak com.lgili.pydracula')