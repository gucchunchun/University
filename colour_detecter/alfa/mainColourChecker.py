from PIL import Image
import cv2
from sklearn.cluster import KMeans
from IPython.display import display
import glob
import os 


def mainColour(sample):
    cv2_img = cv2.imread(sample)

    # cv2はBGR順、pillowはRGBの順のため
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    # (vertical, horizontal,colour channel)-(flatten, colour channel)
    cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))

    cluster = KMeans(n_clusters=5)
    cluster.fit(X=cv2_img)
    cluster_centers_arr = cluster.cluster_centers_.astype(int, copy=False)

    # 幅と高さ64px × 横並び5画像を作ります。
    IMG_SIZE = 64
    width = IMG_SIZE * 5
    height = IMG_SIZE

    tiled_color_img = Image.new(mode='RGB', size=(width, height))

    for k,rgb_arr in enumerate(cluster_centers_arr):
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        color_img = Image.new(mode='RGB', size=(IMG_SIZE, IMG_SIZE), color=color_hex_str)
        tiled_color_img.paste(im=color_img,box=(IMG_SIZE * k, 0))

    return tiled_color_img


# それぞれのウェブサイトにおけるメインカラー５色の特定
# folder = '/Users/yuna/Documents/GE/GEsample/UK/金融'
# samples=glob.glob(folder + '/*.png')
# for i, sample in enumerate(samples):
#     mainColour(sample).save(folder + 'C/pickedColour'+str(i)+'.jpg')
#     os.rename(sample,folder + '/sample'+str(i)+'.png')

# check main colour for each sites
# sites = "Wales"
# mainColour("/Users/yuna/Documents/GE/samplesUni/" + sites + "C/colours.png").save("/Users/yuna/Documents/GE/samplesUni/"+ sites + "C/" + sites +"Main.png")

folder = "/Users/yuna/Documents/GE/GEsample/UK/mainColor"
mainColour(folder + "/colours.png").save(folder + "/Main.png")
