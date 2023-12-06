import cv2, os
from pathlib import Path

def img_sort(imgs_dir,**kwargs):
    extensions = {'.png', '.jpg'}
    keys = {**kwargs}
    for key, value in keys.items():
        if (Path.cwd() / value).is_dir(): continue
        else: os.mkdir(value)

    for path in imgs_dir.glob('*'):
        if path.suffix not in extensions: continue
        print(path)
        cv2.namedWindow("Is this image rotated?")
        img = cv2.imread(str(path), cv2.IMREAD_ANYCOLOR)

        while True:
            cv2.imshow("Is this image rotated?", img)

            k = cv2.waitKey(0)
            kstr = chr(k)
            if kstr in keys:
                
                os.rename(path, (imgs_dir / keys[kstr] / path.name ).resolve())
                break
            elif k == 27:
                break
            else:
                print("please enter j or k : "+kstr)
            
    print("broke")
    cv2.destroyAllWindows() # destroy all windows

if __name__ == "__main__":
    imgs_dir = Path.cwd()
    args = {}
    input_string='''Enter a letter key you want to use as a sort shortcut
    (at least one required, leave blank to run function):'''
    arg = input(input_string)
    while arg:
        key=arg
        value=input("Enter the name of the directory to move images to when you press "+key)
        args[key] = value
        arg = input(input_string)
    img_sort(imgs_dir,**args)