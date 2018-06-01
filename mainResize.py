import os
import traceback
import zipfile

from PIL import Image

extensions = ['JPG']
resize_method = Image.ANTIALIAS

num = [1, 2, 3, 4, 5]
max_height_arr = [348, 375, 480, 800, 1600]
max_width_arr = [235, 250, 320, 525, 1066]

for iNum, jMAX1, zMAX2 in zip(num, max_height_arr, max_width_arr):

    print(iNum, jMAX1, zMAX2)

    path = os.path.abspath("/Users/mghaffari/Desktop/iranoug-session8-image")
    pathSave = path + "/" + jMAX1.__str__() + "x" + zMAX2.__str__()
    pathZipFile = path + '/' + jMAX1.__str__() + "x" + zMAX2.__str__() + '.zip'


    def adjusted_size(width, height):
        if width > jMAX1 or jMAX1 > jMAX1:
            if width > height:
                return jMAX1, int(zMAX2 * height / width)
            else:
                return int(jMAX1 * width / height), jMAX1
        else:
            return width, height


    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))


    if __name__ == "__main__":
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                f_text, f_ext = os.path.splitext(f)
                f_ext = f_ext[1:].upper()
                if f_ext in extensions:
                    print(f)
                    image = Image.open(os.path.join(path, f))
                    width, height = image.size

                    ##region SaveFile
                    if os.path.isdir(pathSave):

                        try:
                            image = image.resize(adjusted_size(width, height))
                            image.save(os.path.join(pathSave, f))

                        except:
                            traceback.print_exc()
                    else:
                        os.mkdir(pathSave)
                        image = image.resize(adjusted_size(width, height))
                        image.save(os.path.join(pathSave, f))

                    # endregion SaveFile
                    zipf = zipfile.ZipFile(pathZipFile, 'w', zipfile.ZIP_DEFLATED)
                    zipdir(pathSave, zipf)
                    zipf.close()
                    # os.rmdir(pathSave)
