pyside6-rcc ./src/pydracula/view/resources.qrc -o ./src/pydracula/view/resources_rc.py

for file in ./src/pydracula/view/*.ui
do
  export OUTPUT_FILE="./src/pydracula/view/$(echo ${file} | sed "s/.*\///" | sed "s/.ui/.py/")"
  echo "Generating ${OUTPUT_FILE}"
  pyside6-uic $file  -o $OUTPUT_FILE
  sed -i 's/_translate = QtCore.QCoreApplication.translate//g' $OUTPUT_FILE
  sed -i 's/_translate(".*", /_(/g' $OUTPUT_FILE
  sed -i '1i\from gettext import gettext as _' $OUTPUT_FILE
  sed -i '/import resources_rc/c\import pydracula.view.resources_rc' $OUTPUT_FILE
done
