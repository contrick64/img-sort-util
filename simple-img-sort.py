import cv2, os
from pathlib import Path

def img_sort(imgs_dir,**kwargs):
    extensions = {'.png', '.jpg','.tif'}
    shortcuts = {**kwargs}
    keys=""

    for key, value in shortcuts.items():
        plural=''
        if keys:
            keys += ", "+key
            plural='s'
        else:
            keys += key
        if (Path.cwd() / value).is_dir(): continue
        else: os.mkdir(value)

    print('''A new window has opened to display your images, you may need to focus it.
Press any of ['''+keys+'''] to sort, spacebar to leave current image in the current working directory, or Esc to break''')
    for path in imgs_dir.glob('*'):
        if path.suffix not in extensions: continue
        print(path)
        cv2.namedWindow("img-sort-util")
        img = cv2.imread(str(path), cv2.IMREAD_ANYCOLOR)

        cv2.imshow("img-sort-util", img)

        while True:
            k = cv2.waitKey(0)
            kstr = chr(k)
            if kstr in shortcuts:
                os.rename(path, (imgs_dir / shortcuts[kstr] / path.name ).resolve())
                print("Moved to ./"+shortcuts[kstr])
                break
            elif kstr == " ":
                print("skip")
                break
            elif k == 27:
                print('end')
                return
            else:
                print("You typed "+kstr+". please use your predefined shortcut key"+plural+": "+keys)
    print("Done.")
    cv2.destroyAllWindows() # destroy all windows

if __name__ == "__main__":
    imgs_dir = Path.cwd()
    args = {}
    input_string='''Enter a directory name for images to be sorted into: '''
    arg = input(input_string)
    while arg:
        value=arg
        key=input("Enter the letter key to use as a shortcut (this will sort images into \""+value+"\"): ")
        args[key] = value
        arg = input("Leave blank to continue... \n"+input_string)
    img_sort(imgs_dir,**args)
