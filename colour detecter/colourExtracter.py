import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import extcolors

from colormap import rgb2hex
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def exact_color(input_image):
    # Dataframeの作成
    colors_x = extcolors.extract_from_path(input_image, tolerance=20, limit=11)
    #([((r.g.b),occurrence),(r.g.b),occurrence)])の形式

    black = 0
    white = 0
    df_rgb = []
    df_percent = []
    for colour in colors_x[0]:
        if colour[0] == (255,255,255):
            white += colour[1]
        elif colour[0] == (0,0,0):
            black += colour[1]
        else:
            df_rgb.append(colour[0])
            df_percent.append(colour[1])


    # RGBからHEXコードへの変換
    df_color_up = [rgb2hex(int(tuple[0]),
                           int(tuple[1]),
                           int(tuple[2])) for tuple in df_rgb]

    df_color = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])


    # 注釈を付ける
    list_color = list(df_color['c_code'])
    list_precent = [int(i) for i in list(df_color['occurence'])]
    text_c = [c + ' ' + str(round(p * 100 / sum(list_precent), 1)) + '%' for c, p in zip(list_color, list_precent)]
    fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(100, 50), dpi=10)

    # donut plot
    wedges, text = ax1.pie(list_precent,
                           labels=text_c,
                           labeldistance=1.05,
                           colors=list_color,
                           textprops={'fontsize': 120, 'color': 'black'})



    #color palette
    x_posi, y_posi, y_posi2 = 160, -170, -170
    for c in list_color:
        if list_color.index(c) <= 5:
            y_posi += 180
            rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor = c)
            ax2.add_patch(rect)
            ax2.text(x = x_posi+400, y = y_posi+100, s = c, fontdict={'fontsize': 190})
        else:
            y_posi2 += 180
            rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor = c)
            ax2.add_artist(rect)
            ax2.text(x = x_posi+1400, y= y_posi2+100, s = c, fontdict={'fontsize': 190})

    ax2.axis('off')

    # fig.set_facecolor('white')
    fig.set_alpha(0.0)
    plt.tight_layout()
    fig.savefig('after_' + input_image, format="png",  transparent=True)
    return plt.show()


exact_color('download.jpeg')

# '/Users/yuna/Documents/GE/samples/results/'+ts