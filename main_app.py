from flask import Flask, render_template, request
import re


app = Flask(__name__)

@app.route('/')
def index():


    c_style = ['探索无限','古风','二次元','写实风格','浮世绘','low poly','未来主义','像素风格','概念艺术','赛博朋克','洛丽塔风格','巴洛克风格','超现实主义','水彩画','蒸汽波艺术','油画','卡通画']
    c_resolution = ['1536*1024','1024*1536','1024*1024']
    c_num = ['1','2','3','4','5','6']


    return render_template('index.html', t_options_style=c_style,t_options_resolution=c_resolution,t_options_num=c_num)





@app.route('/creation',methods=['POST'])
def creation():

    style = request.form['style']
    resolution = request.form['resolution']
    num = request.form['num']
    describe = request.form['describe']

    # 别动
    # 百度的代码
    import wenxin_api
    from wenxin_api.tasks.text_to_image import TextToImage
    wenxin_api.ak = "izBl5cvG4LGMaHIjf9doLgV2rY8PndDZ"
    wenxin_api.sk = "mSidzdTMMWbVS9lxtwKM21LR7Xo67bSB"
    input_dict = {
        "text": describe,
        "style": style,  # 解锁更多风格后，非必选参数
        "resolution": resolution,  # 也可设置为 1024*1536、1536*1024
        "num": num,  # 功能解锁后，可设置的范围为[1,2,3,4,5,6]
    }

    # 返回URL
    # rst = TextToImage.create(**input_dict)

    # 没API了，临时一下
    rst = "{'imgUrls': ['https://wenxin.baidu.com/younger/file/ERNIE-ViLG/57c1dce8e4a5079eaadd440085b2283dex','https://wenxin.baidu.com/younger/file/ERNIE-ViLG/f78f35c9b729d032c5a8f07b1c96f856ex','https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2aed3e3c9491940461a3621113d57826ex','https://wenxin.baidu.com/younger/file/ERNIE-ViLG/023d6e1143e67dac315171fad0d2f02cex','https://wenxin.baidu.com/younger/file/ERNIE-ViLG/70e2df97e131b5b687dd9b218cdea7e8ex','https://wenxin.baidu.com/younger/file/ERNIE-ViLG/9c316c918de06de7945bfe9e0c352173ex']}"

    # 分割
    rst = re.findall("'([^']*)'",rst)


    if num == '1':
        img1=rst[1]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1)
    elif num == '2':
        img1 = rst[1]
        img2 = rst[2]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1,t_img2=img2)
    elif num == '3':
        img1 = rst[1]
        img2 = rst[2]
        img3 = rst[3]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1, t_img2=img2,t_img3=img3)
    elif num == '4':
        img1 = rst[1]
        img2 = rst[2]
        img3 = rst[3]
        img4 = rst[4]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1, t_img2=img2, t_img3=img3,t_img4=img4)
    elif num == '5':
        img1 = rst[1]
        img2 = rst[2]
        img3 = rst[3]
        img4 = rst[4]
        img5 = rst[5]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1, t_img2=img2, t_img3=img3, t_img4=img4,t_img5=img5)
    else:
        img1 = rst[1]
        img2 = rst[2]
        img3 = rst[3]
        img4 = rst[4]
        img5 = rst[5]
        img6 = rst[6]
        return render_template('creation.html', t_describe=describe, t_style=style, t_resolution=resolution, t_num=num,t_rst=rst, t_img1=img1, t_img2=img2, t_img3=img3, t_img4=img4, t_img5=img5,t_img6=img6)






app.run(port=5002, debug=True)
