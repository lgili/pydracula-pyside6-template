pyside6-rcc ./pydracula/view/resources.qrc -o ./pydracula/view/resources_rc.py

for file in ./pydracula/view/*.ui
do
  export OUTPUT_FILE="./pydracula/view/$(echo ${file} | sed "s/.*\///" | sed "s/.ui/.py/")"
  echo "Generating ${OUTPUT_FILE}"
  pyside6-uic $file  -o $OUTPUT_FILE
  sed -i 's/_translate = QtCore.QCoreApplication.translate//g' $OUTPUT_FILE
  sed -i 's/_translate(".*", /_(/g' $OUTPUT_FILE
  sed -i '1i\from gettext import gettext as _' $OUTPUT_FILE
  sed -i '/import resources_rc/c\import pydracula.view.resources_rc' $OUTPUT_FILE
done
