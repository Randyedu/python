Python Imaging Library 中文手册

这是 PIL 的官方手册，2005 年5 月6 日发布。这个版本涵盖 PIL 1.1.5 的全部内
容。本中文手册来自Woodpecker.org.cn 啄木鸟社区
你可以在 PythonWare library 找到改文档其它格式的版本以及先前的版本。
原版出处：http://www.pythonware.com/library/pil/handbook/
目录
1. Python Imaging Library 中文手册
2. 第一部分：介绍
1. 概览
1. 介绍
2. 图像归档处理
3. 图像显示
4. 图像处理
2. 入门导引
1. 使用 Image 类
2. 读写图像
3. 裁剪、粘贴和合并图像
4. 滚动一幅图像
5. 分离与合并通道
3. 几何变换
1. 简单的几何变换
2. transpose 图像
4. 颜色变换
1. 转换图像颜色模式
5. 图像增强
1. 滤波器
1. 使用滤波器
2. 点操作
1. 使用点变换
2. 处理单个通道
3. 增强
1. 增强图像
6. 图像序列
1. 读取图像序列
2. 一个序列迭代类
7. Postscript 格式打印
1. Drawing Postscript
8. 更多关于读取图像
1. 控制解码器
3. 概念
1. 通道
2. 模式
3. 大小
4. 坐标系统
5. 调色板
6. 信息
7. 滤波器
4. 第二部分：模块手册
5. Image 模块
1. 例子
2. 函数
1. new
2. open
3. blend
4. composite
5. eval
6. frombuffer
7. fromstring
8. merge
3. 方法
1. convert
2. copy
3. crop
4. draft
5. filter
6. fromstring
7. getbands
8. getbbox
9. getdata
10. getextrema
11. getpixel
12. histogram
13. load
14. offset
15. paste
16. point
17. putalpha
18. putdata
19. putpalette
20. putpixel
21. resize
22. rotate
23. save
24. seek
25. show
26. split
27. tell
28. thumbnail
29. tobitmap
30. tostring
31. transform
32. transpose
33. verify
4. 属性
1. format
2. mode
3. size
4. palette
5. info
6. ImageChops 模块
1. 函数
1. constant
2. duplicate
3. invert
4. lighter
5. darker
6. difference
7. multiply
8. screen
9. add
10. subtract
11. blend
12. composite
13. offset
7. ImageColor 模块
1. Colour Names
2. 函数
1. getrgb
2. getcolor
8. ImageDraw 模块
1. Example
2. Concepts
1. Coordinates
2. Colour Names
3. Fonts
3. 函数
1. Draw
4. 方法
1. arc
2. bitmap
3. chord
4. ellipse
5. line
6. pieslice
7. point
8. polygon
9. rectangle
10. text
11. textsize
5. Options
1. outline
2. fill
3. font
6. Compatibility
1. ImageDraw
2. setink
3. setfill
4. setfont
9. ImageEnhance 模块
1. Example
2. Interface
3. The Color Class
4. The Brightness Class
5. The Contrast Class
6. The Sharpness Class
10. ImageFile 模块
1. Example
2. 函数
1. Parser
3. 方法
1. feed
11. ImageFileIO 模块
1. 函数
12. ImageFilter 模块
1. Example
2. Filters
1. Kernel
2. RankFilter
3. MinFilter
4. MedianFilter
5. MaxFilter
13. ImageFont 模块
1. 例子
2. 函数
1. load
2. load_path
3. truetype
4. load_default
3. 方法
1. getsize
2. getmask
14. ImageGrab 模块
1. 函数
1. grab
2. grabclipboard
15. ImageOps 模块
1. 函数
1. autocontrast
2. colorize
3. crop
4. deform
5. equalize
6. expand
7. fit
8. flip
9. grayscale
10. invert
11. mirror
12. posterize
13. solarize
16. ImagePath 模块
1. 函数
1. Path
17. ImagePalette 模块
1. 例子
2. 类
1. ImagePalette
18. ImageSequence 模块
1. 函数
1. Iterator
2. 方法
1. Operator []
19. ImageStat 模块
1. 函数
1. Stat
2. Attributes
1. extrema
2. count
3. sum
4. sum2
5. pixel
6. median
7. rms
8. var
9. stddev
20. ImageTk 模块
1. The BitmapImage Class
2. The PhotoImage Class
21. ImageWin 模块
1. Dib 类
1. Dib
2. 方法
1. expose
2. draw
3. palette
4. paste
22. PSDraw 模块
1. Classes
1. PSDraw
2. PSDraw 方法
1. begin
2. end
3. line
4. rectangle
5. text
6. setfont
7. setink
8. setfill
23. ImageCrackCode 模块 (PIL Plus)
1. 函数
1. CrackCode
2. 方法 and attributes
1. area
2. bbox
3. caliper
4. centroid
5. edge
6. links
7. offset
8. start
9. top
10. hit
11. topath
12. getmask
13. getoutline
24. ImageMath 模块 (PIL Plus)
1. 例子
2. 函数
1. eval
3. 表达式语法
1. 运算符
2. 内建函数
25. 第三部分：工具手册
26. pildriver 工具
1. 例子
2. The PILDriver Class
3. 方法
4. pilconvert 工具
5. pilfile 工具
6. pilfont 工具
7. pilprint 工具
27. 附录
1. 软件许可证
2. 技术支持
3. 图像文件格式
4. 编写自己的文件解码器
28. 译注：中英文术语对照表
第一部分：介绍
• PIL 1.1.5 | 2005 年5 月5 日 | Fredrik Lundh
概览
介绍
Python Imaging Library 为 Python 解释器提供了图像处理的功能。
这个库提供了广泛的文件格式支持、高效的内部表示以及相当强大的图像处理
功能。
这个图像处理库的核心被设计成为能够快速访问以几种基本像素类型表示的图
像数据。它为通用图像处理工具提供了一个坚实基础。
让我们来看一些这个库可能的用途：
图像归档处理
Python Imaging Library 适合编写图像归档和批处理应用程序。使用这个库可以
创建缩略图、转换文件格式、打印图像等。
当前版本的库能够识别和读取很多的图像格式。而能够输出的格式被特意限制
于在交换和展示图像中最常用的格式上。
图像显示
当前版本的库包含 Tk 的PhotoImage 和 BitmapImage 接口，也包含 Windows
的DIB 接口（可以同PythonWin 和其他基于Windows 的界面工具包一起使用）。
还有一些其他的PIL 支持提供了很多其他的GUI 工具包。
为了调试方便，库中有一个 show 方法，它把图像保存到磁盘中，并调用外部
显示工具来显示它。
图像处理
这个库提供了基本的图像处理功能，包括点操作、一些内建滤波核的滤波操作
以及颜色空间变换操作。
这个库也支持图像的缩放、旋转及任何仿射（affine）变换。
库中包含一个 histogram 方法，可以从图像中提取某些统计特征。用它可以实现
自动的对比度增强以及全局统计分析功能。
入门导引
使用 Image 类
Python Imaging Library 中最重要的类是Image 类，它定义在与它同名的模块
中。有多种创建这个类的对象的方法：可以从文件中读取得到，也可以从其他
图像经处理得到，或者创建一个全新的。
要从文件读取图像，可以使用 Image 模块提供的open 函数。
切换行号显示
1 >>> import Image
2 >>> im = Image.open("lena.ppm")
3
如果成功，这个函数返回一个 Image 对象。可以使用这个对象的属性来查看文
件的内容。
切换行号显示
1 >>> print im.format, im.size, im.mode
2 PPM (512, 512) RGB
3
format 属性表示图像的原始格式。如果图像不是从文件中读取的，则它被设置
成 None。size 属性是一个2 元组，表示图像的宽度和高度（以像素为单位）。
mode 属性定义图像的色彩通道的数量与名字，同时也包括像素的类型和颜色
深度信息。通常来说，灰度图像的mode 是"L" (luminance)，真彩色图像的mode
是 "RGB" ，而用来打印的图像的mode 是"CMYK"。
如果文件不能打开，会抛出一个 IOError 异常。
一旦有了一个 Image 类的对象，接下来就可以使用这个类定义的方法来处理和
操作图像了。比如说，显示刚才打开的文件：
切换行号显示
1 >>> im.show()
2
（show 的标准实现不是很高效，因为它先将图像保存成一个临时文件，然后
调用 xv 程序来显示图像。如果你没有安装xv ，它甚至不能工作。然而如果
它可用，它将是非常方便的出错和测试的工具。）
接下来的内容将对库中提供的一些函数进行一个概述。
读写图像
Python Imaging Library 支持很广泛的图象文件格式。要从磁盘上读取文件，使
用 Image 模块提供的open 函数。你不必了解你要打开的文件的格式，库会自
动根据文件的内容来确定图像的格式。
要保存文件，使用 Image 类的save 方法。保存文件时，文件名就变得非常重要
了。除非你指定了格式，否则库会根据文件扩展名来决定使用哪种格式存储。
将文件转换成 JPEG
切换行号显示
1 import os, sys
2 import Image
3
4 for infile in sys.argv[1:]:
5 f, e = os.path.splitext(infile)
6 outfile = f + ".jpg"
7 if infile != outfile:
8 try:
9 Image.open(infile).save(outfile)
10 except IOError:
11 print "cannot convert", infile
12
save 方法可以带第二个参数，用来显式指定要保存的文件的格式。如果要使用
非标准的扩展名，就必须这样指定文件格式：
创建 JPEG 缩略图
切换行号显示
1 import os, sys
2 import Image
3
4 size = 128, 128
5
6 for infile in sys.argv[1:]:
7 outfile = os.path.splitext(infile)[0] + ".thumbnail"
8 if infile != outfile:
9 try:
10 im = Image.open(infile)
11 im.thumbnail(size)
12 im.save(outfile, "JPEG")
13 except IOError:
14 print "cannot create thumbnail for", infile
15
有一点非常重要的需要注意的是，除非到了迫不得已的时候，库不会装载或者
解码原始的点阵数据。当打开一个文件的时候，库会读取文件头以获得文件格
式、颜色模式、图像大小等属性，但是文件剩余的部分不会马上处理。
这意味着，文件打开操作是很快的，它与文件的大小、压缩的类型没有关系。
这里是一个快速识别一系列图像文件的简单例子：
识别图像文件
切换行号显示
1 import sys
2 import Image
3
4 for infile in sys.argv[1:]:
5 try:
6 im = Image.open(infile)
7 print infile, im.format, "%dx%d" % im.size, im.mode
8 except IOError:
9 pass
10
裁剪、粘贴和合并图像
Image 类提供一些对图像中的某一区域进行处理的方法。要从图像中提取一块
子矩形区域，使用 crop 方法。
从图像中拷贝一块子矩形区域 ===
切换行号显示
1 box = (100, 100, 400, 400)
2 region = im.crop(box)
3
区域由一个 4 元组定义，表示为坐标是 (left, upper, right, lower)。 Python
Imaging Library 使用左上角为 (0, 0)的坐标系统。同时要注意，这些坐标指向
像素之间的位置，因此上述例子中描述的区域的大小为300x300 像素。
区域图像能够经过某些特定的处理并粘回原处。
处理一块子矩形区域，并粘回原处
切换行号显示
1 region = region.transpose(Image.ROTATE_180)
2 im.paste(region, box)
3
当把区域粘回图像时，指定的区域大小必须和区域图像的大小相同。此外，区
域不能超出图像的边界。然而，原始图像的模式和区域图像的模式不必相同。
如果不相同，区域图像的模式会在粘贴前被自动转换 (细节请查看后面有关颜
色变换的章节)。
这里有另一个例子：
滚动一幅图像
切换行号显示
1 def roll(image, delta):
2 "Roll an image sideways"
3
4 xsize, ysize = image.size
5
6 delta = delta % xsize
7 if delta == 0: return image
8
9 part1 = image.crop((0, 0, delta, ysize))
10 part2 = image.crop((delta, 0, xsize, ysize))
11 image.paste(part2, (0, 0, xsize-delta, ysize))
12 image.paste(part1, (xsize-delta, 0, xsize, ysize))
13
14 return image
15
更高级的技巧是，paste 方法可以带一个透明掩模作为可选参数。在这个掩模
中，像素值255 代表被粘贴的图像在那个位置上是不透明的。 (就是说，此处
显示被粘贴的图像上的值。)像素值 0 表示被粘贴的图像是完全透明的。在它
们之间的值表示不同程度的透明度。
Python Imaging Library 还允许对一幅多通道图像（比如RGB 图像）的单个通
道进行操作。split 方法能够创建一组新的图像，每一幅都是原来多通道图像的
一个通道。merge 函数以一个模式和一组图像的元组为参数，把这些图像组成
一幅新图像。下面的例子实现交换一幅RGB 图像的三个通道：
分离与合并通道
切换行号显示
1 r, g, b = im.split()
2 im = Image.merge("RGB", (b, g, r))
3
几何变换
Image 类包含resize 和 rotate 方法来缩放和旋转图像。前者带一个tuple 类型
的参数来表示新的图像大小，后者带一个逆时针旋转的角度值作为参数。
简单的几何变换
切换行号显示
1 out = im.resize((128, 128))
2 out = im.rotate(45) # degrees counter-clockwise
3
如果要将图像旋转 90 度的整数倍，可以使用rotate 或者transpose 方法。后者
还可以用来水平或者垂直镜像一幅图像。
transpose 图像
切换行号显示
1 out = im.transpose(Image.FLIP_LEFT_RIGHT)
2 out = im.transpose(Image.FLIP_TOP_BOTTOM)
3 out = im.transpose(Image.ROTATE_90)
4 out = im.transpose(Image.ROTATE_180)
5 out = im.transpose(Image.ROTATE_270)
6
There's no difference in performance or result between transpose(ROTATE) and
corresponding rotate operations.
一个更通用的变换方法是 transform，在参考手册中有对它的详细叙述。
颜色变换
Python Imaging Library 提供convert 函数，可以将图像在不同的像素格式间转
换。
转换图像颜色模式
切换行号显示
1 im = Image.open("lena.ppm").convert("L")
2
库支持在所有支持的颜色模式和"L"以及"RGB"之间的直接转换。其他颜色模
式之间的转换要借助于中间图像模式（通常是"RGB" 模式）。
图像增强
Python Imaging Library 提供一系列的函数和模块来进行图像增强。
滤波器
ImageFilter 模块中包含一些预定义的增强滤波器，用 filter 方法来使用滤波
器。
使用滤波器
切换行号显示
1 import ImageFilter
2 out = im.filter(ImageFilter.DETAIL)
3
点操作
point 方法可以对图像的像素值进行变换（比如对比度变换）。在大多数场合，
使用函数对象（带一个参数）作为参数传递给point 方法。每一个像素使用这个
函数对象进行变换：
使用点变换
切换行号显示
1 # multiply each pixel by 1.2
2 out = im.point(lambda i: i * 1.2)
3
用上面的技巧，你可以对图像用任何简单的表达式进行变换。你还可以结合使
用point 和paste 方法来有选择的改变一幅图像：
处理单个通道
切换行号显示
1 # split the image into individual bands
2 source = im.split()
3
4 R, G, B = 0, 1, 2
5
6 # select regions where red is less than 100
7 mask = source[R].point(lambda i: i < 100 and 255)
8
9 # process the green band
10 out = source[G].point(lambda i: i * 0.7)
11
12 # paste the processed band back, but only where red was < 100
13 source[G].paste(out, None, mask)
14
15 # build a new multiband image
16 im = Image.merge(im.mode, source)
17
注意用来创建 mask 的语法：
切换行号显示
1 imout = im.point(lambda i: expression and 255)
2
Python 只计算一个逻辑表达式的一部分，只要能确定表达式的结果其他部分就
不进行计算了，并把最后计算得到的值作为表达式的值返回。因此，如果上述
expression 是false(0)，Python 就不会检查第二个参数，因此返回0，否则返回
255。
增强
对于更多更高级的图像增强，可以使用 ImageEnhance 模块。一旦从图像上创
建了增强对象，你就可以尝试采用各种不同的参数进行快速的增强处理了。
你能通过这样的方法来调整图像的对比度、亮度、色彩平衡和锐度。
增强图像
切换行号显示
1 import ImageEnhance
2
3 enh = ImageEnhance.Contrast(im)
4 enh.enhance(1.3).show("30% more contrast")
5
图像序列
Python Imaging Library 包含对于图像序列 (也称作动画格式)的基本支持。支
持的序列格式包括 FLI/FLC, GIF, 和一些试验性的格式。TIFF 文件也能包含
超过一帧的图像。
当你打开一个序列文件时，PIL 会自动加载序列中的第一帧。你可以使用seek
和tell 方法在不同帧之间移动：
读取图像序列
切换行号显示
1 import Image
2
3 im = Image.open("animation.gif")
4 im.seek(1) # skip to the second frame
5
6 try:
7 while 1:
8 im.seek(im.tell()+1)
9 # do something to im
10 except EOFError:
11 pass # end of sequence
12
正如这个例子所示，当序列结束时，你会得到一个 EOFError 异常。
注意，当前版本库的绝大多数驱动只允许你移动到下一帧(如上面例子所示)。
如果要回到文件的开头，你可能必须重新打开它。
下面的迭代类让你能够使用 for 循环来迭代图像序列：
一个序列迭代类
切换行号显示
1 class ImageSequence:
2 def __init__(self, im):
3 self.im = im
4 def __getitem__(self, ix):
5 try:
6 if ix:
7 self.im.seek(ix)
8 return self.im
9 except EOFError:
10 raise IndexError # end of sequence
11
12 for frame in ImageSequence(im):
13 # ...do something to frame...
14
Postscript 格式打印
Python Imaging Library 提供将图像、文字和图形输出到Postscript 打印机的功
能。这是一个简单的例子：
Drawing Postscript
切换行号显示
1 import Image
2 import PSDraw
3
4 im = Image.open("lena.ppm")
5 title = "lena"
6 box = (1*72, 2*72, 7*72, 10*72) # in points
7
8 ps = PSDraw.PSDraw() # default is sys.stdout
9 ps.begin_document(title)
10
11 # draw the image (75 dpi)
12 ps.image(box, im, 75)
13 ps.rectangle(box)
14
15 # draw centered title
16 ps.setfont("HelveticaNarrow-Bold", 36)
17 w, h, b = ps.textsize(title)
18 ps.text((4*72-w/2, 1*72-h), title)
19
20 ps.end_document()
21
更多关于读取图像
前面叙述过，Image 模块的open 函数用来打开一个图像文件。在大多数情况，
你只用简单的把文件名传给它就可以了：
切换行号显示
1 im = Image.open("lena.ppm")
2
如果一切正常，结果是一个 Image 对象。否则，会抛出一个IOError 异常。
你可以使用一个类似文件的对象来代替文件名。这个对象必须实现read、 seek
和 tell 方法，并以二进制方式打开。从一个打开的文件读取
切换行号显示
1 fp = open("lena.ppm", "rb")
2 im = Image.open(fp)
3
要从字符串数据中读取一幅图像，可以使用 StringIO 类： 从一个字符串读取
切换行号显示
1 import StringIO
2
3 im = Image.open(StringIO.StringIO(buffer))
4
注意库在读取图像头之前，会先移动到文件头 (用seek(0))。另外，在图像数据
被读取 (通过 load 方法)以后，seek 方法也会被调用。如果图像文件被嵌在一
个更大的文件里面，比如tar 文件，你可以使用ContainerIO 或者TarIO 模块
来访问它。从一个 tar 压缩文档读取
切换行号显示
1 import TarIO
2
3 fp = TarIO.TarIO("Imaging.tar", "Imaging/test/lena.ppm")
4 im = Image.open(fp)
5
控制解码器
一些解码器允许你在从文件读取图像的同时对图像进行操作。这个特性常常被
用来在创建缩略图（创建缩略图的速度通常比缩略图的质量更重要）或者打印
到一个黑白激光打印机（只需要图像的灰度信息）时加速图像的解码。
draft 方法能够操作一个没有被载入数据的图像对象，使得它能够尽可能与需
要的模式和大小相匹配。这通过重新配置图像解码器来实现。以草稿方式读
取
切换行号显示
1 im = Image.open(file)
2 print "original =", im.mode, im.size
3
4 im.draft("L", (100, 100))
5 print "draft =", im.mode, im.size
6
这个程序可能会打印出这样的结果：
切换行号显示
1 original = RGB (512, 512)
2 draft = L (128, 128)
3
注意，最终获得图像可能与要求的模式和大小不完全一致。如果要求生成的图
像不能超过给定的大小，可以使用thumbnail 方法来代替。
概念
• Python Imaging Library 处理光栅图像（raster images），即方型的像素
数据。
通道
一幅图像可以有一个或者多个通道的数据构成。Python Imaging Library 允许在
一个图像中存储多个通道，只要这些通道的大小和颜色深度都是一样的。
要获取图像的通道数目和通道名称，可以使用
[image.htm#image-getbands-method getbands] 方法。
模式
图像的模式定义了图像的像素的类型和颜色深度。当前版本的库支持下列标准
模式：
• 1 (1-bit 像素, 黑白, 一个像素存储为一个字节)
• L (8-bit 像素, 黑白)
• P (8-bit 像素, 使用调色板映射到其他任一模式)
• RGB (3x8-bit 像素, 真彩色)
• RGBA (4x8-bit 像素, 带透明掩模的真彩色)
• CMYK (4x8-bit 像素, colour separation)
• YCbCr (3x8-bit 像素, colour video format)
• I (32-bit integer 像素)
• F (32-bit floating point 像素)
PIL 还支持一些特殊的模式，包括RGBX (true colour with padding)和
RGBa (true colour with premultiplied alpha)。
你可以通过[image.htm#image-mode-attribute mode]属性读取图像的模式，它是
一个包含上述模式类型值的字符串。
大小
通过图像的[image.htm#image-size-attribute size]属性可以读取图像的大小信息。
大小信息由一个包含水平和垂直像素数的二元组表示。
坐标系统
Python Imaging Library 使用笛卡尔像素坐标系统，原点 (0,0)在图像的左上
角。注意：坐标值对应像素的左上角，像素(0, 0)实际中心位于(0.5, 0.5)。
坐标通常以 2 元组(x, y)的形式传递给库。矩形则表示成4 元组的形式，左上角
为第一个。比如，覆盖整个800x600 像素的矩形表示为(0, 0, 800, 600)。
调色板
调色板模式 ("P")使用一个彩色调色板来定义每个像素的真实颜色。
信息
你可以使用[image.htm#image-info-attribute info]属性在图像中添加辅助的信
息。这是一个字典对象。
在读取和存储文件时如何处理这些信息是和文件的类型有关系的（查看
[formats.htm 图像文件格式]这一章）。
滤波器
对于将多个输入像素映射到一个输出像素的几何变换操作，Python Imaging
Library 提供了四种重采用滤波器。
* NEAREST
在输入图像中选择最近的点，忽略其他所有点。
* BILINEAR
在输入图像的 2x2 像素范围内进行线性插值。注意当前版本的PIL 中，
这个滤波器在下采样时使用固定的输入范围的大小。
* BICUBIC
在输入图像的 4x4 像素范围内进行三次插值。注意当前版本的PIL 中，
这个滤波器在下采样时使用固定的输入范围的大小。
* ANTIALIAS
(在PIL 1.1.3 中新增)。使用高质量的重采样滤波器(a truncated sinc)对
所有可能影响结果的输入像素进行计算来得到输出像素的值。在当前版
本的PIL 中，这个滤波器只能在resize 和 thumbnail 方法中使用。
注意，当前版本的 PIL 中，只有ANTIALIAS 滤波器是唯一在下采样（把一幅较
大的图像转换成较小的图像）时能正常工作的滤波器。BILINEAR 和BICUBIC
滤波器使用固定的输入范围大小，适用在保持比例(scale-preserving?)的几何转
换或者上采样时。
第二部分：模块手册
Image 模块
Image 模块提供了一个同名的类，用来表示一个 PIL 图像。这个模块同时提供
了一些工厂函数，包括从文件读取图像的函数以及创建新图像的函数。
例子
下面的脚本读取一幅图像，旋转 45 度，再把它在Unix 上用xv 显示出来，或者
在Windows 上用paint 显示出来。
打开、旋转、显示图像 (使用默认的图像浏览器)
import Image im = Image.open("bride.jpg") im.rotate(45).show()
• 下面的脚本创建当前目录中所有 JPEG图像的128x128的缩略图。创建缩
略图
import glob for infile in glob.glob("*.jpg"): file, ext =
os.path.splitext(infile) im = Image.open(infile)
im.thumbnail((128, 128), Image.ANTIALIAS) im.save(file +
".thumbnail", "JPEG")
函数
new
• Image.new(mode, size) => image
Image.new(mode, size, color) => image
• 使用给定的模式和大小创建一个新图像。大小是以 2 元组的形式给出
的。当创建单通道的图时，color 是单个值；当创建多通道图像时，
color 是一个元组（每个通道一个值）。如果color 参数缺省，图像被填充
成全黑。如果color 是None，则图像不被初始化。
open
• Image.open(infile) => image
Image.open(infile, mode) => image
• 打开并识别给定的图像文件。这是一个会被延迟（lazy）的操作；实际的
图像数据并不马上从文件中读入，而是等到需要处理这些数据的时候才
被读入 (可以调用load 方法强制读入数据)。如果要指定mode 参数，则
mode 必须是"r"。
o 你可以使用一个字符串（表示文件名）或者一个文件对象作为
infile。在用文件对象时，文件对象必须实现read, seek, 和tell 方
法，而且必须用二进制模式打开。
blend
• Image.blend(image1, image2, alpha) => image
o 对两幅图像用固定的透明度（alpha）插值生成新的图像。输入的
两幅图像必须是同样的大小和模式。
out = image1 * (1.0 - alpha) + image2 * alpha
如果alpha 是0.0，则会返回第一幅图像的一个拷贝。如果alpha 是1.0，
则会返回第二幅图像的一个拷贝。alpha 的取值范围没有限制。如果必
要，计算结果会被裁减到允许的输出值的范围。
composite
• Image.composite(image1, image2, mask) => image 对两幅图像用图像mask
作为透明度插值生成新的图像。 mask 图像可以是"1", "L", 或者
"RGBA"模式。所有的图像必须是同样的大小。
eval
• Image.eval(function, image) => image 将函数（应该带一个参数）作用于给
定图像的每一个像素。如果图像有多个通道，这个函数会作用于每一个
通道。注意，这个函数对于同样的像素值只会被调用一次，因此你不能
使用一个随机函数或者其它的像素生成函数来作为函数。
frombuffer
• Image.frombuffer(mode, size, data) => image
(PIL 1.1.4 alpha 4中新增。) 对字符串或者缓冲区对象包含的像素数据，
使用标准的"raw"解码器来创建图像。。对于某些模式，图像内存可以
与原始缓冲区共享同一块内存 (这意味着如果修改原始的缓冲区对象，
将会对图像产生影响)。不是所有的模式都能够共享内存；支持的模式包
括"L"、"RGBX"、"RGBA"和"CMYK"。对于其他模式，这个函数和
fromstring 函数作用相同。
Image.frombuffer(mode, size, data, decoder, parameters) => image
与对应的 fromstring 函数调用相同。
fromstring
• Image.fromstring(mode, size, data) => image 从字符串中读取像素数据，使
用标准的"raw"解码器创建图像。
Image.fromstring(mode, size, data, decoder, parameters) => image
o 与前一个函数的区别是，这个函数允许使用你使用任意 PIL 支持
的像素解码器来解码数据。更多有关解码器的信息，参看
[decoder.htm 编写自己的文件解码器]。
注意，这个函数只是解码像素数据，而不是解码整个图像。如果要处理
存在字符串中的完整图像，可以使用StringIO 把字符串包装起来然后用
open 方法来装载它。
merge
• Image.merge(mode, bands) => image
o 从一组单通道的图像创建一幅新图像。通道用图像的元组或者列
表的形式给出，每一项是模式mode描述的一个通道。所有通道的
大小必须相同。
方法
Image 类的对象有下列方法。除非特别声明，所有的方法返回一个新的Image
类型对象，包含处理的结果。
convert
• im.convert(mode) => image
o 返回转换后的图象拷贝。对于"P"模式，这种转换通过调色板进
行。如果模式被省略，那么该方法会自动选取一个能够保存所有
图像信息和不需要调色板来表示的图像模式。
当前版本的库支持"L"、"RGB"和"CMYK"模式之间的相互转换。当把
一幅彩色图像转换成灰度图象（模式"L"），库使用 ITU-R 601-2 两度转
换公式：
L = R * 299/1000 + G * 587/1000 + B * 114/1000
当把一幅灰度图象转换成 2 值图像（模式"1"）时，所有非零值都被转换
成255（白）。要使用其它阈值，可以使用point 方法。
o im.convert(mode, matrix) => image
将"RGB"模式图像使用一个转换矩阵转换成"RGB"或者"L"模式图像。
矩阵是一个四元组或者16 元组。下面的例子将 RGB 图像 (根据 ITU-R
709 使用 D65 亮度进行过线性校正) 转换成 CIE XYZ 颜色空间图像：
Convert RGB to XYZ
rgb2xyz = ( 0.412453, 0.357580, 0.180423, 0,
0.212671, 0.715160, 0.072169, 0, 0.019334, 0.119193,
0.950227, 0 ) out = im.convert("RGB", rgb2xyz)
copy
• im.copy() => image 拷贝图像。使用这个函数把其它东西粘贴到图像中，
并保留原来的图像不变。
crop
• im.crop(box) => image
o 返回当前图像的一个矩形区域。box 是一个四元组指定左、上、
右、下四个边界的坐标。
这是一个会被延迟（lazy）的操作。改变原始的图像可能会影响到剪裁生
成的图像。为消除这种影响，可以调用裁剪生成的图象的load 方法。
draft
• im.draft(mode, size) 配置图像装载器使其能够返回与指定模式尽可能接近
的图像。比如说，你可以使用这个函数，将彩色JPEG 图像在装载的时
候转换成灰度图象，或者从PCD文件中解出128x192 的图像。注意，这
个方法会改变调用的Image 对象。如果图像已经被装入，这个方法没有
任何作用。
filter
• im.filter(filter) => image
o 返回当前图像经过给定滤波器滤波后的图像。 要查看可用的滤
波器，参考ImageFilter 模块。
fromstring
• im.fromstring(data)
im.fromstring(data, decoder, parameters)
• 与 fromstring 函数基本相同，只是将data 装入当前图像。
getbands
• im.getbands() => tuple of strings
o 返回包含每个通道的名字的元组。比如，在 RGB 图像上调用
getbands 返回("R", "G", "B")。
getbbox
• im.getbbox() => 4-tuple or None
Calculates the bounding box of the non-zero regions in the image. The bounding
box is returned as a 4-tuple defining the left, upper, right, and lower pixel
coordinate. If the image is completely empty, this method returns None.
getdata
• im.getdata() => sequence
o 返回以像素值序列的形式返回当前图像的内容。图像的像素值从
第零行开始被一行一行的连接在一起变成一维线性的序列对象。
注意，这个方法返回的序列对象是 PIL 内部数据类型，只支持部分序列
操作。可以使用list(im.getdata())将其转换为普通的序列对象（比如需要
打印）。
getextrema
• im.getextrema() => 2-tuple 返回一个二元组包含图像的最小值和最大值。
当前版本的PIL 中这个方法仅支持单通道图像。
getpixel
• im.getpixel(xy) => value or tuple 返回指定位置的像素值。如果图像是多层
（multi-layer）图像，该方法返回一个元组。
注意，这个方法相当慢；如果你需要处理大量的图像数据，使用getdata
方法。
histogram
• im.histogram() => list
• 返回图像的直方图。直方图是原图像中每一种像素值的个数的列表。如
果图像有多于一个通道，那么所有通道的直方图被连接在一起。（比
如，"RGB"图像的直方图包含768 个值。）
o 二值图像(模式"1")在这个方法中被作为灰度图像(模式"L")来处
理。
im.histogram(mask) => list
o 返回图像中对应掩模图像是非零的那些像素的直方图。掩模图像
必须和原图像同样大小，并且必须是二值图像(模式"1")或者灰度
图像(模式"L")。
load
• im.load() 分配图像数据的存储空间，并将数据从文件读入（或对于其它被
推迟的操作，从源图像读入）。在通常情况下，你不需要调用这个方
法。因为当被打开的图像第一次访问数据时，它会自动装入数据。
offset
• im.offset(xoffset, yoffset) => image
o (过期的)返回图像数据被平移给定的偏移量以后的图像。Data
wraps around the edges. If yoffset is omitted, it is assumed to be
equal to xoffset.
这个方法以后将不被支持。新代码应该使用
[imagechops.htm#offset ImageChops]模块提供的offset 函数。
paste
• im.paste(image, box)
Pastes another image into this image. The box argument is either a 2-tuple giving
the upper left corner, a 4-tuple defining the left, upper, right, and lower pixel
coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted
image must match the size of the region.
If the modes don't match, the pasted image is converted to the mode of this image
(see the convert method for details).
im.paste(colour, box)
Same as above, but fills the region with a single colour. The colour is given as a
single numerical value for single-band images, and a tuple for multi-band images.
im.paste(image, box, mask)
Same as above, but updates only the regions indicated by the mask. You can use
either "1", "L" or "RGBA" images (in the latter case, the alpha band is used as
mask). Where the mask is 255, the given image is copied as is. Where the mask is 0,
the current value is preserved. Intermediate values can be used for transparency
effects.
Note that if you paste an "RGBA" image, the alpha band is ignored. You can work
around this by using the same image as both source image and mask.
im.paste(colour, box, mask)
Same as above, but fills the region indicated by the mask with a single colour.
point
• im.point(table) => image
im.point(function) image => image
Returns a copy of the image where each pixel has been mapped through the given
table. The table should contains 256 values per band in the image. If a function is
used instead, it should take a single argument. The function is called once for each
possible pixel value, and the resulting table is applied to all bands of the image.
If the image has mode "I" (integer) or "F" (floating point), you must use a
function, and it must have the following format:
argument * scale + offset
Map floating point images
out = im.point(lambda i: i * 1.2 + 10)
You can leave out either the scale or the offset.
im.point(table, mode) => image
im.point(function, mode) => image
Map the image through table, and convert it on fly. In the current version of PIL ,
this can only be used to convert "L" and "P" images to "1" in one step, e.g. to
threshold an image.
putalpha
• im.putalpha(band)
Copies the given band to the alpha layer of the current image. The image must be
an "RGBA" image, and the band must be either "L" or "1".
putdata
• im.putdata(data)
im.putdata(data, scale, offset)
Copy pixel values from a sequence object into the image, starting at the upper left
corner (0, 0). The scale and offset values are used to adjust the sequence values:
pixel = value * scale + offset
If the scale is omitted, it defaults to 1.0. If the offset is omitted, it defaults to 0.0.
putpalette
• im.putpalette(sequence)
Attach a palette to a "P" or "L" image. The palette sequence should contain 768
integer values, where each group of three values represent the red, green, and blue
values for the corresponding pixel index. Instead of an integer sequence, you can
use an 8-bit string.
putpixel
• im.putpixel(xy, colour)
Modifies the pixel at the given position. The colour is given as a single numerical
value for single-band images, and a tuple for multi-band images.
Note that this method is relatively slow. For more extensive changes, use paste or
the ImageDraw module instead.
resize
• im.resize(size) => image
im.resize(size, filter) => image
Returns a resized copy of an image. The size argument gives the requested size in
pixels, as a 2-tuple: (width, height).
The filter argument can be one of NEAREST (use nearest
neighbour), BILINEAR (linear interpolation in a 2x2
environment), BICUBIC (cubic spline interpolation in a 4x4 environment),
or ANTIALIAS (a high-quality downsampling filter). If omitted, or if the image has
mode "1" or "P", it is set to NEAREST.
rotate
• im.rotate(angle) => image
im.rotate(angle, filter) => image
Returns a copy of an image rotated the given number of degrees counter clockwise
around its centre.
The filter argument can be one of NEAREST (use nearest
neighbour), BILINEAR (linear interpolation in a 2x2 environment),
or BICUBIC (cubic spline interpolation in a 4x4 environment). If omitted, or if the
image has mode "1" or "P", it is set to NEAREST.
save
• im.save(outfile, options)
im.save(outfile, format, options)
• 用给定的文件名保存图像。如果 format 没有指定，将用文件扩展名来决
定格式。这个方法返回None。
Keyword options can be used to provide additional instructions to the writer. If a
writer doesn't recognise an option, it is silently ignored. The available options are
described later in this handbook.
You can use a file object instead of a filename. In this case, you must always specify
the format. The file object must implement the seek, tell, and write methods, and be
opened in binary mode.
seek
• im.seek(frame)
Seeks to the given frame in a sequence file. If you seek beyond the end of the
sequence, the method raises an EOFError exception. When a sequence file is
opened, the library automatically seeks to frame 0.
Note that in the current version of the library, most sequence formats only allows
you to seek to the next frame.
show
• im.show() 显示图像。这个方法主要用作调试目的。
在 Unix 平台上，这个方法把图像保存为一个临时的PPM 文件，然后调
用xv 工具。
在 Windows平台上，它将图像保存为一个临时的BMP文件，并使用系统
默认的BMP 显示工具来显示它(通常是Paint)。
o 这个方法返回 None。
split
• im.split() => sequence
Returns a tuple of individual image bands from an image. For example, splitting an
"RGB" image creates three new images each containing a copy of one of the
original bands (red, green, blue).
tell
• im.tell() => integer
o 返回当前图像帧的序号。
thumbnail
• im.thumbnail(size)
im.thumbnail(size, filter)
Modifies the image to contain a thumbnail version of itself, no larger than the given
size. This method calculates an appropriate thumbnail size to preserve the aspect of
the image, calls the draft method to configure the file reader (where applicable),
and finally resizes the image.
The filter argument can be one of NEAREST, BILINEAR, BICUBIC,
or ANTIALIAS (best quality). If omitted, it defaults to NEAREST (this will be
changed to ANTIALIAS in future versions).
Note that the bilinear and bicubic filters in the current version of PIL are not
well-suited for thumbnail generation. You should use ANTIALIAS unless speed is
much more important than quality.
Also note that this function modifies the Image object in place. If you need to use
the full resolution image as well, apply this method to a copy of the original image.
This method returns None.
tobitmap
• im.tobitmap() => string
Returns the image converted to an X11 bitmap.
tostring
• im.tostring() => string
Returns a string containing pixel data, using the standard "raw" encoder.
im.tostring(encoder, parameters) => string
Returns a string containing pixel data, using the given data encoding.
transform
• im.transform(size, method, data) => image
im.transform(size, method, data, filter) => image
• 用给定的大小、与原图像相同的模式创建一个新图像，新图象的数据为
原图像数据经过给定的变换而得到。
o 在当前版本的 PIL 中，method 参数可以是EXTENT（剪切一个矩
形区域）、AFFINE（仿射变换）、QUAD（map a quadrilateral to a
rectangle）或者MESH（map a number of source quadrilaterals in one
operation）。不同的方法的区别如下。
filter 参数定义如何从源图像进行像素滤波得到目标像素。当前版
本中这个参数可以是NEAREST（使用最近的像素），BILINEAR（使
用2x2 大小的双线性插值）、BICUBIC（使用4x4 大小的三次样条
插值）。如果这个参数省略，或者图像是"1"模式或者"P"模式
的，这个参数将被设置成NEAREST。
im.transform(size, EXTENT, data) => image
im.transform(size, EXTENT, data, filter) => image
• 从图像中提取一个子区域。
Data 是一个四元组 (x0, y0, x1, y1)，指定输入图像上的两个点的坐标。
结果图像将包含这两个点之间的数据，源图像上的 (x0, y0)成为目标图
像上的 (0,0)， 源图像上的(x1, y1)变成size。
o 这个方法可以用来切割、拉伸、缩小或者镜像当前图像中的任意
矩形区域。这个方法比crop 稍慢，但是和对应的resize 差不多
快。
im.transform(size, AFFINE, data) => image
im.transform(size, AFFINE, data, filter) => image
• 对图像进行仿射变换，并把结果存在给定大小的图象中。
• Data 是一个 6 元组 (a, b, c, d, e, f)，包含了仿射变换矩阵的前两行参
数。对于结果图像上的每一个像素点 (x, y)，像素值从源图像上的
(a x + b y + c, d x + e y + f)位置取得。
o 这个函数可以用来对源图像进行缩放、平移、旋转和 shear 变
换。
im.transform(size, QUAD, data) => image
im.transform(size, QUAD, data, filter) => image
• 将图像上一个四边形 (有四个角定义的一个区域) 映射到一个给定大小
的矩形中。
Data 是一个 8 元组 (x0, y0, x1, y1, x2, y2, y3, y3)，依次指定源图像上区
域的左上角、左下角，右下角和右上角的坐标。
im.transform(size, MESH, data) image => image
im.transform(size, MESH, data, filter) image => image
• 类似于 QUAD，只是data 是一个目标矩形区域和对应源图像上的四边形
的列表。
transpose
• im.transpose(method) => image
o 返回一个原始图像镜像的或者旋转的图像。
method 参数可以是：FLIP_LEFT_RIGHT、FLIP_TOP_BOTTOM、
ROTATE_90、ROTATE_180 或者ROTATE_270。
verify
• im.verify()
• 使用这个函数来确定文件是否有损坏，但是并不对图像数据进行解码。
如果这个函数发现问题，它将抛出异常。如果在使用这个函数后要读取
图像数据，则必须重新打开这个图像文件。
属性
Image 类的对象包含以下属性：
format
• im.format => string or None
o 源文件的文件格式。如果是由库创建的图像，这个属性是 None。
mode
• im.mode => string 图像的模式。这是一个指定图像使用的像素格式的字
符串。最常使用的模式是"1"、"L"、"RGB"以及"CMYK"。
size
• im.size => (width, height)
o 图像的大小，以像素为单位。大小由一个二元组 (宽度, 高度)来
表示。
palette
• im.palette => palette or None
如果有调色板的话，这个属性指向颜色调色板。如果模式是"P"， 它指
向的是ImagePalette 类的一个对象。否则，它是 None。
info
• im.info => dictionary
• 包含图像相关数据的字典。
ImageChops 模块
The ImageChops module contains a number of arithmetical image operations,
called channel operations ("chops"). These can be used for various purposes,
including special effects, image compositions, algorithmic painting, and more.
At this time, channel operations are only implemented for 8-bit images (e.g. "L"
and "RGB").
函数
Most channel operations take one or two image arguments and returns a new
image. Unless otherwise noted, the result of a channel operation is always clipped
to the range 0 to MAX (which is 255 for all modes supported by the operations in
this module).
constant
ImageChops.constant(image, value) => image
Return a layer with the same size as the given image, but filled with the given pixel
value.
duplicate
ImageChops.duplicate(image) => image
Return a copy of the given image.
invert
ImageChops.invert(image) => image
Inverts an image.
• out = MAX - image
lighter
ImageChops.lighter(image1, image2) => image
Compares the two images, pixel by pixel, and returns a new image containing the
lighter values.
• out = max(image1, image2)
darker
ImageChops.darker(image1, image2) => image
Compares the two images, pixel by pixel, and returns a new image containing the
darker values.
• out = min(image1, image2)
difference
ImageChops.difference(image1, image2) => image
Returns the absolute value of the difference between the two images.
• out = abs(image1 - image2)
multiply
ImageChops.multiply(image1, image2) => image
Superimposes two images on top of each other. If you multiply an image with a
solid black image, the result is black. If you multiply with a solid white image, the
image is unaffected.
• out = image1 * image2 / MAX
screen
ImageChops.screen(image1, image2) => image
Superimposes two inverted images on top of each other.
• out = MAX - ((MAX - image1) * (MAX - image2) / MAX)
add
ImageChops.add(image1, image2, scale, offset) => image
Adds two images, dividing the result by scale and adding the offset. If omitted, scale
defaults to 1.0, and offset to 0.0.
• out = (image1 + image2) / scale + offset
subtract
ImageChops.subtract(image1, image2, scale, offset) => image
Subtracts two images, dividing the result by scale and adding the offset. If omitted,
scale defaults to 1.0, and offset to 0.0.
• out = (image1 - image2) / scale + offset
blend
ImageChops.blend(image1, image2, alpha) => image
Same as the blend function in the Image module.
composite
ImageChops.composite(image1, image2, mask) => image
Same as the composite function in the Image module.
offset
ImageChops.offset(xoffset, yoffset) => image
ImageChops.offset(offset) => image
Returns a copy of the image where data has been offset by the given distances. Data
wraps around the edges. If yoffset is omitted, it is assumed to be equal to xoffset.
ImageColor 模块
The ImageColor module contains colour tables and converters from CSS3-style
colour specifiers to RGB tuples. This module is used by Image.new and
the ImageDraw module, among others.
Colour Names
The ImageColor module supports the following string formats:
• Hexadecimal color specifiers, given as "#rgb" or "#rrggbb". For example,
"#ff0000" specifies pure red.
• RGB functions, given as "rgb(red, green, blue)" where the colour values are
integers in the range 0 to 255. Alternatively, the color values can be given as
three percentages (0% to 100%). For example, "rgb(255,0,0)" and
"rgb(100%,0%,0%)" both specify pure red.
• Hue-Saturation-Lightness (HSL) functions, given as "hsl(hue, saturation%,
lightness%)" where hue is the colour given as an angle between 0 and 360
(red=0, green=120, blue=240), saturation is a value between 0% and 100%
(gray=0%, full color=100%), and lightness is a value between 0% and 100%
(black=0%, normal=50%, white=100%). For example, "hsl(0,100%,50%)"
is pure red.
• Common HTML colour names. The ImageColor module provides some 140
standard colour names, based on the colors supported by the X Window
system and most web browsers. Colour names are case insensitive. For
example, "red" and "Red" both specify pure red.
函数
getrgb
getrgb(color) => (red, green, blue)
(New in 1.1.4) Convert a colour string to an RGB tuple. If the string cannot be
parsed, this function raises a ValueError exception.
getcolor
getcolor(color, mode) => (red, green, blue) or integer
(New in 1.1.4) Same as getrgb, but converts the RGB value to a greyscale value if
the mode is not color or a palette image. If the string cannot be parsed, this
function raises a ValueError exception.
ImageDraw 模块
The ImageDraw module provide simple 2D graphics for Image objects. You can use
this module to create new images, annotate or retouch existing images, and to
generate graphics on the fly for web use.
Example
Draw a Grey Cross Over an Image
import Image, ImageDraw
im = Image.open("lena.pgm")
draw = ImageDraw.Draw(im) draw.line((0, 0) + im.size, fill=128) draw.line((0,
im.size[1], im.size[0], 0), fill=128) del draw
# write to stdout im.save(sys.stdout, "PNG")
Concepts
Coordinates
The graphics interface uses the same coordinate system as PIL itself, with (0, 0) in
the upper left corner. Colours
To specify colours, you can use numbers or tuples just as you would use with
Image.new or Image.putpixel. For "1", "L", and "I" images, use integers. For
"RGB" images, use a 3-tuple containing integer values. For "F" images, use
integer or floating point values.
For palette images (mode "P"), use integers as colour indexes. In 1.1.4 and later,
you can also use RGB 3-tuples or colour names (see below). The drawing layer will
automatically assign colour indexes, as long as you don't draw with more than 256
colours.
Colour Names
In PIL 1.1.4 and later, you can also use string constants when drawing in "RGB"
images. PIL supports the following string formats:
• Hexadecimal color specifiers, given as "#rgb" or "#rrggbb". For example,
"#ff0000" specifies pure red.
• RGB functions, given as "rgb(red, green, blue)" where the colour values are
integers in the range 0 to 255. Alternatively, the color values can be given as
three percentages (0% to 100%). For example, "rgb(255,0,0)" and
"rgb(100%,0%,0%)" both specify pure red.
• Hue-Saturation-Lightness (HSL) functions, given as "hsl(hue, saturation%,
lightness%)" where hue is the colour given as an angle between 0 and 360
(red=0, green=120, blue=240), saturation is a value between 0% and 100%
(gray=0%, full color=100%), and lightness is a value between 0% and 100%
(black=0%, normal=50%, white=100%). For example, "hsl(0,100%,50%)"
is pure red.
• Common HTML colour names. The ImageDraw provides some 140
standard colour names, based on the colors supported by the X Window
system and most web browsers. Colour names are case insensitive, and may
contain whitespace. For example, "red" and "Red" both specify pure red.
Fonts
PIL can use bitmap fonts or OpenType/TrueType fonts.
Bitmap fonts are stored in PIL's own format, where each font typically consists of a
two files, one named .pil and the other usually named .pbm. The former contains
font metrics, the latter raster data.
To load a bitmap font, use the load functions in the ImageFont module.
To load a OpenType/TrueType font, use the truetype function in
the ImageFont module. Note that OpenType/TrueType support is optional, and may
not be supported by all PIL builds.
函数
Draw
Draw(image) => Draw instance
Creates an object that can be used to draw in the given image.
Note that the image will be modified in place.
方法
arc
draw.arc(xy, start, end, options)
Draws an arc (a portion of a circle outline) between the start and end angles, inside
the given bounding box.
The outline option gives the colour to use for the arc.
bitmap
draw.bitmap(xy, bitmap, options)
Draws a bitmap at the given position, using the current fill colour.
chord
draw.chord(xy, start, end, options)
Same as arc, but connects the end points with a straight line.
The outline option gives the colour to use for the chord outline. The fill option gives
the colour to use for the chord interior.
ellipse
draw.ellipse(xy, options)
Draws an ellipse inside the given bounding box.
The outline option gives the colour to use for the ellipse outline. The fill option
gives the colour to use for the ellipse interior.
line
draw.line(xy, options)
Draws a line between the coordinates in the xy list.
The coordinate list can be any sequence object containing either 2-tuples [ (x, y), ... ]
or numeric values [ x, y, ... ]. It should contain at least two coordinates.
The fill option gives the colour to use for the line.
pieslice
draw.pieslice(xy, start, end, options)
Same as arc, but also draws straight lines between the end points and the center of
the bounding box.
The outline option gives the colour to use for the pieslice outline. The fill option
gives the colour to use for the pieslice interior.
point
draw.point(xy, options)
Draws points (individual pixels) at the given coordinates.
The coordinate list can be any sequence object containing either 2-tuples [ (x, y), ... ]
or numeric values [ x, y, ... ].
The fill option gives the colour to use for the points.
polygon
draw.polygon(xy, options)
Draws a polygon.
The polygon outline consists of straight lines between the given coordinates, plus a
straight line between the last and the first coordinate.
The coordinate list can be any sequence object containing either 2-tuples [ (x, y), ... ]
or numeric values [ x, y, ... ]. It should contain at least three coordinates.
The outline option gives the colour to use for the polygon outline. The fill option
gives the colour to use for the polygon interior.
rectangle
draw.rectangle(box, options)
Draws a rectangle.
The box can be any sequence object containing either 2-tuples [ (x, y), (x, y) ] or
numeric values [ x, y, x, y ]. It should contain two coordinates.
Note that the second coordinate pair defines a point just outside the rectangle, also
when the rectangle is not filled.
The outline option gives the colour to use for the rectangle outline. The fill option
gives the colour to use for the rectangle interior.
text
draw.text(position, string, options)
Draws the string at the given position. The position gives the upper right corner of
the text.
The font option is used to specify which font to use. It should be an instance of
the ImageFont class, typically loaded from file using the load method in
the ImageFont module.
The fill option gives the colour to use for the text.
textsize
draw.textsize(string, options) => (width, height)
Return the size of the given string, in pixels.
The font option is used to specify which font to use. It should be an instance of
the ImageFont class, typically loaded from file using the load method in
the ImageFont module.
Options
outline
outline integer or tuple
fill
fill integer or tuple
font
font ImageFont instance
Compatibility
The Draw class contains a constructor and a number of methods which are
provided for backwards compatibility only. For this to work properly, you should
either use options on the drawing primitives, or these methods. Do not mix the old
and new calling conventions.
ImageDraw
ImageDraw(image) => Draw instance
(Deprecated). Same as Draw. Don't use this name in new code.
setink
draw.setink(ink)
(Deprecated). Sets the colour to use for subsequent draw and fill operations.
setfill
draw.setfill(mode)
(Deprecated). Sets the fill mode.
If the mode is 0, subsequently drawn shapes (like polygons and rectangles) are
outlined. If the mode is 1, they are filled.
setfont
draw.setfont(font)
(Deprecated). Sets the default font to use for the text method.
The font argument should be an instance of the ImageFont class, typically loaded
from file using the load method in the ImageFont module.
ImageEnhance 模块
The ImageEnhance module contains a number of classes that can be used for
image enhancement.
Example
Vary the Sharpness of an Image
import ImageEnhance
enhancer = ImageEnhance.Sharpness(image)
for i in range(8):
• factor = i / 4.0 enhancer.enhance(factor).show("Sharpness %f" % factor)
See the enhancer.py demo program in the Scripts directory.
Interface
All enhancement classes implement a common interface, containing a single
method:
enhancer.enhance(factor) => image
Returns an enhanced image. The factor is a floating point value controlling the
enhancement. Factor 1.0 always returns a copy of the original image, lower factors
mean less colour (brightness, contrast, etc), and higher values more. There are no
restrictions on this value.
The Color Class
The colour enhancement class is used to adjust the colour balance of an image, in a
manner similar to the controls on a colour TV set. This class implements the
enhancement interface as described above.
ImageEnhance.Color(image) => Color enhancer instance
Creates an enhancement object for adjusting colour in an image. A factor of 0.0
gives a black and white image, a factor of 1.0 gives the original image.
The Brightness Class
The brightness enhancement class is used to control the brightness of an image.
ImageEnhance.Brightness(image) => Brightness enhancer instance
Creates an enhancement object for adjusting brightness in an image. A factor of 0.0
gives a black image, factor 1.0 gives the original image.
The Contrast Class
The contrast enhancement class is used to control the contrast of an image, similar
to the contrast control on a TV set.
ImageEnhance.Contrast(image) => Contrast enhancer instance
Creates an enhancement object for adjusting contrast in an image. A factor of 0.0
gives an solid grey image, factor 1.0 gives the original image.
The Sharpness Class
The sharpness enhancement class is used to control the sharpness of an image.
ImageEnhance.Sharpness(image) => Sharpness enhancer instance
Creates an enhancement object for adjusting the sharpness of an image. The factor
0.0 gives a blurred image, 1.0 gives the original image, and a factor of 2.0 gives a
sharpened image.
ImageFile 模块
The ImageFile module provides support functions for the image open and save
functions.
In addition, it provides a Parser class which can be used to decode an image piece
by piece (e.g. while receiving it over a network connection). This class implements
the same consumer interface as the standard sgmllib and xmllib modules.
Example
Parse An Image
import ImageFile
fp = open("lena.pgm", "rb")
p = ImageFile.Parser()
while 1:
• s = fp.read(1024) if not s:
o break
p.feed(s)
im = p.close()
im.save("copy.jpg")
函数
Parser
ImageFile.Parser() => Parser instance
Creates a parser object. Parsers cannot be reused.
方法
feed
parser.feed(data)
Feed a string of data to the parser. This method may raise an IOError
exception. close
parser.close() => image or None
Tells the parser to finish decoding. If the parser managed to decode an image, it
returns an Image object. Otherwise, this method raises an IOError exception.
Note: If the file cannot be identified the parser will raise an IOError exception in
the close method. If the file can be identified, but not decoded (for example, if the
data is damaged, or if it uses an unsupported compression method), the parser will
raise an IOError exception as soon as possible, either in feed or close.
ImageFileIO 模块
ImageFileIO 模块可以用来从套接字或者任何其它流设备读取图像。
这个模块已经被 deprecated。新的代码应该使用ImageFile 模块提供的Parser 类
来代替。
函数
ImageFileIO.ImageFileIO(stream)
为刘文件对象添加缓存，以提供Image.open 方法所需要的seek 和 tell 方法。
流对象必须实现 read 和 close 方法。
ImageFilter 模块
The ImageFilter module contains definitions for a pre-defined set of filters, which
can be be used in conjuction with the filter method of the Image class.
Example
Filter an Image
import ImageFilter
im1 = im.filter(ImageFilter.BLUR)
im2 = im.filter(ImageFilter.MinFilter(3)) im3 = im.filter(ImageFilter.MinFilter) #
same as MinFilter(3)
Filters
The current version of the library provides the following set of predefined image
enhancement filters:
BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, and SHARPEN.
Kernel
Kernel(size, kernel, scale=None, offset=0)
(New in 1.1.5) Create a convolution kernel of the given size. In the current version,
the size must be either (3, 3) or (5, 5), and the kernel argument must be a sequence
containing 9 or 25 integer or floating point weights.
If the scale argument is given, the result of applying the kernel to each pixel is
divided by the scale value. The default is the sum of the kernel weights.
If the offset argument is given, the value is added to the result, after it has been
divided by the scale.
RankFilter
RankFilter(size, rank)
(New in 1.1.5) Create a rank filter of the given size. For each pixel in the input
image, the rank filter sorts all pixels in a (size, size) environment, and copies the
rank'th value to the output image.
MinFilter
MinFilter(size=3)
(New in 1.1.5) Create a min filter of the given size. For each pixel in the input
image, this filter copies the smallest pixel value from a (size, size) environment to
the output image.
MedianFilter
MedianFilter(size=3)
(New in 1.1.5) Create a min filter of the given size. For each pixel in the input
image, this filter copies the smallest pixel value from a (size, size) environment to
the output image.
MaxFilter
MaxFilter(size=3)
(New in 1.1.5) Create a max filter of the given size. For each pixel in the input
image, this filter copies the largest pixel value from a (size, size) environment to the
output image.
ImageFont 模块
The ImageFont module defines a class with the same name. Instances of this class
store bitmap fonts, and are used with the text method of the ImageDraw class.
PIL uses it's own font file format to store bitmap fonts. You can use the pilfont
utility to convert BDF and PCF font descriptors (X window font formats) to this
format.
Starting with version 1.1.4, PIL can be configured to
support TrueType and OpenType fonts. For earlier version, TrueType support is
only available as part of the imToolkit package.
例子
Here's a simple example:
import ImageFont, ImageDraw
font = ImageFont.load("arial.pil")
draw = ImageDraw.Draw(image) draw.text((10, 10), "hello", font=font)
函数
load
ImageFont.load(file) => Font instance
Loads a font from the given file, and returns the corresponding font object. If this
function fails, it raises an IOError exception.
load_path
ImageFont.load_path(file) => Font instance
Same as load, but searches for the file along sys.path if it's not found in the current
directory.
truetype
ImageFont.truetype(file, size) => Font instance
Load a TrueType or OpenType font file, and create a font object. This function
loads a font object from the given file, and creates a font object for a font of the
given size.
On Windows, if the given file name does not exist, the loader also looks in Windows
fonts directory.
This function requires the _imagingft service.
load_default
ImageFont.load_default() => Font instance
(New in 1.1.4) Load a "better than nothing" default font.
方法
Font objects must implement the following methods, which are used by
the ImageDraw layer.
getsize
font.getsize(text) => (width, height)
Returns the width and height of the given text, as a 2-tuple.
getmask
font.getmask(text) => Image object
Returns a bitmap for the text. The bitmap should be an internal PIL storage
memory instance (as defined by the Image.core interface module).
If the font uses antialiasing, the bitmap should have mode "L" and use a maximum
value of 255. Otherwise, it should have mode "1".
ImageGrab 模块
The ImageGrab module can be used to copy the contents of the screen or the
clipboard to a PIL image memory.
The current version works on Windows only.
函数
grab
ImageGrab.grab() => image
ImageGrab.grab(bbox) => image
(New in 1.1.3) Take a snapshot of the screen, and return an "RGB" image. The
bounding box argument can be used to copy only a part of the screen.
grabclipboard
ImageGrab.grabclipboard() => image or list of strings or None
(New in 1.1.4) Take a snapshot of the clipboard contents, and return an image
object or a list of file names. If the clipboard doesn't contain image data, this
function returns None.
You can use isinstance to check if the function returned a valid image object, or
something else:
切换行号显示
1 im = ImageGrab.grabclipboard()
2
3 if isinstance(im, Image.Image):
4 ... got an image ...
5 elif im:
6 for filename in im:
7 try:
8 im = Image.open(filename)
9 except IOError:
10 pass # ignore this file
11 else:
12 ... got an image ...
13 else:
14 ... clipboard empty ...
15
ImageOps 模块
(New in 1.1.3) The ImageOps module contains a number of 'ready-made' image
processing operations. This module is somewhat experimental, and most operators
only work on L and RGB images.
函数
autocontrast
ImageOps.autocontrast(image, cutoff=0) => image
Maximize (normalize) image contrast. This function calculates a histogram of the
input image, removes cutoff percent of the lightest and darkest pixels from the
histogram, and remaps the image so that the darkest pixel becomes black (0), and
the lightest becomes white (255).
colorize
ImageOps.colorize(image, black, white) => image
Colorize grayscale image. The black and white arguments should be RGB tuples or
color names; this function calculates a colour wedge mapping all black pixels in the
source image to the first colour, and all white pixels to the second colour.
crop
ImageOps.crop(image, border=0) => image
Remove border pixels from all four edges. This function works on all image modes.
deform
ImageOps.deform(image, deformer) => image
Deform the image using the given deformer object.
equalize
ImageOps.equalize(image) => image
Equalize the image histogram. This function applies a non-linear mapping to the
input image, in order to create a uniform distribution of grayscale values in the
output image.
expand
ImageOps.expand(image, border=0, fill=0) => image
Add border pixels of border to the image, at all four edges.
fit
ImageOps.fit(image, size, method, bleed, centering) => image
Returns a sized and cropped version of the image, cropped to the requested aspect
ratio and size. The size argument is the requested output size in pixels, given as a
(width, height) tuple.
The method argument is what resampling method to use. The default is
Image.NEAREST (nearest neighbour).
The bleed argument allows you to remove a border around the outside the image
(from all four edges). The value is a decimal percentage (use 0.01 for one percent).
The default value is 0 (no border).
The centering argument is used to control the cropping position. (0.5, 0.5) is center
cropping (i.e. if cropping the width, take 50% off of the left side (and therefore 50%
off the right side), and same with top/bottom).
(0.0, 0.0) will crop from the top left corner (i.e. if cropping the width, take all of the
crop off of the right side, and if cropping the height, take all of it off the bottom).
(1.0, 0.0) will crop from the bottom left corner, etc. (i.e. if cropping the width, take
all of the crop off the left side, and if cropping the height take none from the top
(and therefore all off the bottom)).
The fit function was contributed by Kevin Cazabon.
flip
ImageOps.flip(image) => image
Flip the image vertically (top to bottom).
grayscale
ImageOps.grayscale(image) => image
Convert the image to grayscale.
invert
ImageOps.invert(image) => image
Invert (negate) the image.
mirror
ImageOps.mirror(image) => image
Flip image horizontally (left to right).
posterize
ImageOps.posterize(image, bits) => image
Reduce the number of bits for each colour channel.
solarize
ImageOps.solarize(image, threshold=128) => image
Invert all pixel values above the given threshold.
ImagePath 模块
ImagePath 模块用来存储和操作二维向量数据。路径对象可以被传到
ImageDraw 模块中的方法中。
函数
Path
ImagePath.Path(coordinates) => Path instance
创建一个路径对象。坐标表coordinates 可以是任何包含2 元组 [ (x, y), ... ] 或者
数字值 [ x, y, ... ]的序列对象。
ImagePalette 模块
要使用 ImagePalette 类和相关的函数，要导入 ImagePalette 模块。
例子
将调色板添加到图像
import ImagePalette
im.putpalette(ImagePalette.ImagePalette("RGB"))
类
ImagePalette
ImagePalette.ImagePalette(mode="RGB") => palette instance
这个构造函数创建一个调色板，将"P"模式映射到指定的模式。调色板被初始
化成线性灰度的斜面（译注：索引值0 映射为灰度0，索引值1 映射为灰度1，
以此类推）。
ImageSequence 模块
ImageSequence 模块包含让你能够跌代一个图像序列的包装类。
函数
Iterator
ImageSequence.Iterator(image) => Iterator instance
创建一个Iterator 对象让你可以循环遍历一个序列中的所有帧。
方法
Iterator 类实现 [] 运算符。
Operator []
你可以用大于等于0 的整数作参数调用这个运算符。如果没有足够的帧，跌代
子会抛出一个IndexError 异常。
ImageStat 模块
The ImageStat module calculates global statistics for an image, or for a region of
an image.
函数
Stat
ImageStat.Stat(image) => Stat instance
ImageStat.Stat(image, mask) => Stat instance
Calculates statistics for the give image. If a mask is included, only the regions
covered by that mask are included in the statistics.
ImageStat.Stat(list) => Stat instance
Same as above, but calculates statistics for a previously calculated histogram.
Attributes
The following attributes contain a sequence with one element for each layer in the
image. All attributes are lazily evaluated; if you don't need a value, it won't be
calculated.
extrema
stat.extrema
(Attribute). Get min/max values for each band in the image.
count
stat.count
(Attribute). Get total number of pixels.
sum
stat.sum
(Attribute). Get sum of all pixels.
sum2
stat.sum2
(Attribute). Squared sum of all pixels.
pixel
stat.mean
(Attribute). Average pixel level.
median
stat.median
(Attribute). Median pixel level.
rms
stat.rms
(Attribute). RMS (root-mean-square).
var
stat.var
(Attribute). Variance.
stddev
stat.stddev
(Attribute). Standard deviation.
ImageTk 模块
The ImageTk module contains support to create and modify
Tkinter BitmapImage and PhotoImage objects.
For examples, see the demo programs in the Scripts directory.
The BitmapImage Class
ImageTk.BitmapImage(image, options) => BitmapImage instance
Create a Tkinter-compatible bitmap image, which can be used everywhere Tkinter
expects an image object.
The given image must have mode "1". Pixels having value 0 are treated as
transparent. Options, if any, are passed to Tkinter. The most commonly used option
is foreground, which is used to specify the colour for the non-transparent parts. See
the Tkinter documentation for information on how to specify colours.
The PhotoImage Class
ImageTk.PhotoImage(image) => PhotoImage instance
Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter
expects an image object. If the image is an RGBA image, pixels having alpha 0 are
treated as transparent.
ImageTk.PhotoImage(mode, size) => PhotoImage instance
Same as above, but creates an empty (transparent) photo image object. Use paste to
copy image data to this object.
photo.paste(image, box)
Pastes an image into the photo image. The box is a 4-tuple defining the left, upper,
right, and lower pixel coordinate. If the box is omitted, or None, all of the image is
assumed. In all cases, the size of the pasted image must match the size of the region.
If the image mode does not match the photo image mode, conversions are
automatically applied.
ImageWin 模块
The ImageWin module contains support to create and display images on Windows.
It can be used with PythonWin as well as other user interface toolkits that provides
access to Windows device contexts.
Dib 类
Dib
ImageWin.Dib(image) => Dib instance
ImageWin.Dib(mode, size) => Dib instance
This constructor creates a Windows bitmap from a PIL image, or from a given
mode and size.
The mode can be one of "1", "L", or "RGB".
If the display requires a palette, this constructor creates a suitable palette and
associates it with the image. For an "L" image, 128 greylevels are allocated. For an
"RGB" image, a 6x6x6 colour cube is used, together with 20 greylevels.
To make sure that palettes work properly under Windows, you must call the palette
method upon certain events from Windows. See the method descriptions below.
方法
expose
dib.expose(hdc)
Expose (draw) the image using the given device context handle. The handle is an
integer representing a Windows HDC handle.
In PythonWin, you can use the GetHandleAttrib method of the CDC class to get a
suitable handle.
draw
dib.draw(hdc, destination)
dib.draw(hdc, destination, source)
Same as expose, but allows you to specify where to draw the image, and what part
of it to draw.
The destination and source areas are given as 4-tuple rectangles. If the source is
omitted, the entire image is copied. If the source and the destination have different
sizes, the image is resized as necessary.
palette
dib.palette(handle)
Installs the palette associated with the image in the given device context. The
handle argument is an integer representing a Windows HDC handle.
This method should be called upon QUERYNEWPALETTE and
PALETTECHANGED events from Windows. If this method returns a non-zero
value, one or more display palette entries were changed since the last updated, and
the image should be redrawn.
paste
dib.paste(image, bbox)
Paste an image into the bitmap image. The bbox argument is a 4-tuple defining the
left, upper, right, and lower pixel coordinate. If None is used instead of a tuple, the
entire image is copied. In all cases, the size of the pasted image must match the size
of the region. If the image mode does not match the bitmap mode, conversions are
automatically applied.
PSDraw 模块
The PSDraw module provides simple print support for Postscript printers. You can
print text, graphics and images through this module.
Classes
PSDraw
PSDraw.PSDraw(file) => PSDraw instance
Sets up printing to the given file. If file is omitted, sys.stdout is assumed.
PSDraw 方法
begin
ps.begin_document()
Sets up printing of a document.
end
ps.end_document()
Ends printing.
line
ps.line(from, to)
Draws a line between the two points. Coordinates are given in Postscript point
coordinates (72 points per inch, (0, 0) is the lower left corner of the page).
rectangle
ps.rectangle(box)
Draws a rectangle.
text
ps.text(position, text)
ps.text(position, text, alignment)
Draws text at the given position. You must use setfont before calling this method.
setfont
ps.setfont(font, size)
Selects which font to use. The font argument is a Postscript font name, the size
argument is given in points.
setink
ps.setink(ink)
Selects the pixel value to use with subsequent operations.
setfill
ps.setfill(onoff)
Selects if subsequent rectangle operations should draw filled rectangles or just
outlines.
ImageCrackCode 模块 (PIL Plus)
The ImageCrackCode module allows you to detect and measure features in an
image. This module is only available in the PIL Plus package.
函数
CrackCode
CrackCode(image, position) => CrackCode instance
Identifies a feature in the given image. If the position is omitted, the constructor
searches from the top left corner.
方法 and attributes
area
cc.area
(attribute). The feature area, in pixels.
bbox
cc.bbox
(attribute). The bounding box, given as a 4-tuple (left, upper, right, lower).
caliper
cc.caliper
(attribute). The caliper size, given as a 2-tuple (height, width).
centroid
cc.centroid
(attribute). The center of gravity.
edge
cc.edge
(attribute). True if the feature touches the edges of the image, zero otherwise.
links
cc.links
(attribute). The number of links in the crack code chain.
offset
cc.offset
(attribute). The offset from the upper left corner of the image, to the feature's
bounding box,
start
cc.start
(attribute). The first coordinate in the crack code chain.
top
cc.top
(attribute). The topmost coordinate in the crack code chain.
hit
cc.hit(xy) => flag
Check if the given point is inside this feature.
topath
cc.topath(xy) => path
Return crack code outline as an ImagePath object.
getmask
cc.getmask() => image
Get filled feature mask, as an image object.
getoutline
cc.getoutline() => image
Get feature outline, as an image object.
ImageMath 模块 (PIL Plus)
ImageMath 模块可以用来计算"图像表达式"。这个模块仅提供一个eval 函数，
它带一个表达式串以及一幅或多幅图像作参数。
这个模块仅在 PIL Plus 包中可用。
例子
函数
eval
eval(expression, environment) => image or value
在给定的environment中计算表达式，并返回结果。结果是一幅图像或者是单个
数值(整数、浮点数或一个像素元组)。
表达式语法
表达式是标准的 Python 表达式，但它们是在非标准的环境中计算的。你可以像
平常一样使用一般的PIL 方法，也可以使用下列运算符和函数：
运算符
内建函数
第三部分：工具手册
pildriver 工具
The pildriver tool gives access to most PIL functions from your operating system's
command-line interface.
$ pildriver program
When called as a script, the command-line arguments are passed to a PILDriver
instance (see below). If there are no command-line arguments, the module runs an
interactive interpreter, each line of which is split into space-separated tokens and
passed to the execute method.
The pildriver tool was contributed by Eric S. Raymond.
例子
The following example loads test.png, crops out a portion of its upper-left-hand
corner and displays the cropped portion:
$ pildriver show crop 0 0 200 300 open test.png
The following example loads test.tiff, rotates it 30 degrees, and saves the result as
rotated.png (in PNG format):
$ pildriver save rotated.png rotate 30 open test.tiff
The PILDriver Class
The pildriver module provides a single class called PILDriver.
An instance of the PILDriver class is essentially a software stack machine
(Polish-notation interpreter) for sequencing PIL image transformations. The state
of the instance is the interpreter stack.
The only method one will normally invoke after initialization is the execute method.
This takes an argument list of tokens, pushes them onto the instance's stack, and
then tries to clear the stack by successive evaluation of PILdriver operators. Any
part of the stack not cleaned off persists and is part of the evaluation context for the
next call of the execute method.
PILDriver doesn't catch any exceptions, on the theory that these are actually
diagnostic information that should be interpreted by the calling code.
方法
In the method descriptions below, each line lists a command token, followed by
<>-enclosed arguments which describe how the method interprets the entries on the
stack. Each argument specification begins with a type specification: either int, float,
string, or image.
All operations consume their arguments off the stack (use dup to keep copies
around). Use verbose 1 to see the stack state displayed before each operation.
add <image:pic1> <image:pic2> <int:offset> <float:scale>
• Pop the two top images, produce the scaled sum with offset.
blend <image:pic1> <image:pic2> <float:alpha>
• Replace two images and an alpha with the blended image.
brightness <image:pic1>
• Enhance brightness in the top image.
clear
• Clear the stack.
color <image:pic1>
• Enhance colour in the top image.
composite <image:pic1> <image:pic2> <image:mask>
• Replace two images and a mask with their composite.
contrast <image:pic1>
• Enhance contrast in the top image.
convert <string:mode> <image:pic1>
• Convert the top image to the given mode.
copy <image:pic1>
• Make and push a true copy of the top image.
crop <int:left> <int:upper> <int:right> <int:lower> <image:pic1>
• Crop and push a rectangular region from the current image.
darker <image:pic1> <image:pic2>
• Pop the two top images, push an image of the darker pixels of both.
difference <image:pic1> <image:pic2>
• Pop the two top images, push the difference image
draft <string:mode> <int:xsize> <int:ysize>
• Configure the loader for a given mode and size.
dup
• Duplicate the top-of-stack item.
filter <string:filtername> <image:pic1>
• Process the top image with the given filter.
format <image:pic1>
• Push the format of the top image onto the stack.
getbbox
• Push left, upper, right, and lower pixel coordinates of the top image.
extrema
• Push minimum and maximum pixel values of the top image.
invert <image:pic1>
• Invert the top image.
lighter <image:pic1> <image:pic2>
• Pop the two top images, push an image of the lighter pixels of both.
merge <string:mode> <image:pic1> [<image:pic2> [<image:pic3>
[<image:pic4>]]]
• Merge top-of stack images in a way described by the mode.
mode <image:pic1>
• Push the mode of the top image onto the stack.
multiply <image:pic1> <image:pic2>
• Pop the two top images, push the multiplication image.
new <int:xsize> <int:ysize> <int:color>:
• Create and push a greyscale image of given size and colour.
offset <int:xoffset> <int:yoffset> <image:pic1>
• Offset the pixels in the top image.
open <string:filename>
• Open the indicated image, read it, push the image on the stack.
paste <image:figure> <int:xoffset> <int:yoffset> <image:ground>
• Paste figure image into ground with upper left at given offsets.
pop
• Discard the top element on the stack.
resize <int:xsize> <int:ysize> <image:pic1>
• Resize the top image.
rotate <int:angle> <image:pic1>
• Rotate image through a given angle
save <string:filename> <image:pic1>
• Save image with default options.
save2 <string:filename> <string:options> <image:pic1>
• Save image with specified options.
screen <image:pic1> <image:pic2>
• Pop the two top images, superimpose their inverted versions.
sharpness <image:pic1>
• Enhance sharpness in the top image.
show <image:pic1>
• Display and pop the top image.
size <image:pic1>
• Push the image size on the stack as (y, x).
subtract <image:pic1> <image:pic2> <int:offset> <float:scale>
• Pop the two top images, produce the scaled difference with offset.
swap
• Swap the top-of-stack item with the next one down.
thumbnail <int:xsize> <int:ysize> <image:pic1>
• Modify the top image in the stack to contain a thumbnail of itself.
transpose <string:operator> <image:pic1>
• Transpose the top image.
verbose <int:num>
• Set verbosity flag from top of stack.
pilconvert 工具
pilconvert 工具把图像从一种格式转换成另一种格式。输出格式使用了 -c 选项
来显式指定。如果没有指定，由目标的扩展名来决定。
$ pilconvert lena.tif lena.png $ pilconvert -c JPEG lena.tif lena.tmp
pilfile 工具
pilfile 工具能够识别图像文件，对于能够识别的图像，它能显示图像的格式、
大小和模式。
$ pilfile *.tif lena.tif: TIFF 128x128 RGB
使用-i 选项来显示info 属性。使用-t 选项来显示tile descriptor (which contains
information used to load the image)(译注：PIL1.1.5 并无此选项)。
pilfont 工具
pilfont 工具将BDF 或 PCF 点阵字体文件转换成PIL 的ImageFont 模块能够
使用的格式。
$ pilfont *.pdf
pilprint 工具
pilprint 工具用来打印图像到任何PostScript level 1 打印机。图像会被打印在页
面的中央，上面有文件名(除掉路径和扩展名)。输出会被写到标准输出。
$ pilprint lena.tif | lpr -h
你可以使用-p 选项来直接通过 lpr 和-c 选项打印到一个彩色打印机 (如果不
是彩色打印机，彩色图像会在打印前先被转换成灰度图象)。
附录
软件许可证
Python Imaging Library：
• Copyright © 1997-2003 by Secret Labs AB Copyright © 1995-2003 by
Fredrik Lundh
取得、使用并/或拷贝这个软件以及/或者与此相关的文档，就意味着你阅读、
理解以下条款，并会照做：
只要在所有的拷贝中出现上述保全信息，并在相应的文档中保留上述版权信息
和这个许可信息， Secret Labs AB 或者作者的名字没有出现在未被事先明确、
书面许可的广告或与软件发布相关的公共宣传信息中，则允许为了任何目的使
用、拷贝和发布这个软件及其相关的文档并不需要支付费用。
By obtaining, using, and/or copying this software and/or its associated
documentation, you agree that you have read, understood, and will comply with the
following terms and conditions:
Permission to use, copy, modify, and distribute this software and its associated
documentation for any purpose and without fee is hereby granted, provided that the
above copyright notice appears in all copies, and that both that copyright notice and
this permission notice appear in supporting documentation, and that the name of
Secret Labs AB or the author not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior permission.
SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT
SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
USE OR PERFORMANCE OF THIS SOFTWARE.
技术支持
Patches, fixes, updates, and new utilities are welcome. If you stumble upon files
that the library does not handle as expected, post a note to the Image SIG mailing
list (see below). If you fix such a problem and supply a patch, you may send me the
image file anyway so I don't mess things up again in later revisions.
Ideas on formats and features that should be added, sample files, and other
contributions are also welcome.
For all sorts of updates, including information on commercial support and
extensions to PIL, check the PIL product page, at:
• http://www.pythonware.com/products/pil
You may also find information related to PIL at http://www.pythonware.com or via
the Python home page http://www.python.org
For support and general questions, send e-mail to the Python Image SIG mailing
list:
• image-sig@python.org
You can join the Image SIG by sending a mail to image-sig-request@python.org.
Put subscribe in the message body to automatically subscribe to the list, or help to
get additional information.
Alternatively, you can use the Python mailing list, python-list@python.org, or the
newsgroup comp.lang.python.
图像文件格式
Python Imaging Library 支持很广泛的光栅文件格式。PIL 库差不多能识别和读
取30 种文件格式。输出格式的支持没有这么广泛，但最常用的交换和展示的格
式还是支持的。
open 函数能够从文件的内容识别文件的格式，而不是根据文件名来识别。但
是save 方法会查看文件名来决定使用哪种格式，除非文件格式被显示的指
定。格式描述 BMP
PIL 能够读写包含"1", "L", "P", 或者"RGB"类型数据的Windows 和 OS/2
的BMP 文件。16 色图像按照"P"模式处理。不支持行程编码（Run-length
encoding）。
open 方法设置以下info 属性：
compression
• 如果文件使用行程编码，则此属性设置成"bmp_rle"。
CUR (只读)
CUR 是在Windows 中用来存储指针的格式。 CUR 解码器能读取最大可能的
指针。不支持指针动画指针。 DCX (只读)
DCX is a container file format for PCX files, defined by Intel. The DCX format is
commonly used in fax applications. The DCX decoder files containing "1", "L",
"P", or "RGB" data. Only the first image is read. EPS (只写)
The library identifies EPS files containing image data. It can also write EPS
images. FLI, FLC (只读)
The library reads Autodesk FLI and FLC animations.
open 方法会设置以下info 属性：
duration
• The delay (in milliseconds) between each frame.
FPX (只读)
The library reads Kodak FlashPix files. In the current version, only the highest
resolution image is read from the file, and the viewing transform is not taken into
account.
Note: To enable full FlashPix support, you need to build and install the IJG JPEG
library before building the Python Imaging Library. See the distribution README
for details. GBR (只读)
The GBR decoder reads GIMP brush files.
open 方法会设置以下info 属性：
description
• The brush name.
GD (只读)
The library reads GD uncompressed files. Note that this file format cannot be
automatically identified, so you must use the open function in
the GdImageFile module to read such a file.
open 方法会设置以下info 属性：
transparency
• Transparency colour index. This key is omitted if the image is not
transparent.
GIF
库能够读取 GIF87a 和GIF89a 版本的 GIF 文件格式。保存文件时库会使用
行程编码的 GIF87a 格式文件。注意 GIF 文件总是作为调色板模式 ("P")图
像被读取的。
open 方法会设置以下info 属性：
version
• 版本（("GIF87a" 或 "GIF89a"）。
transparency
• 透明色的索引。如果图像是不透明的，这个键值被忽略。
ICO (只读)
ICO is used to store icons on Windows. The largest available icon is read. IM
IM is a format used by LabEye and other applications based on the IFUNC image
processing library. The library reads and writes most uncompressed interchange
versions of this format.
IM is the only format that can store all internal PIL formats. IMT (只读)
The library reads Image Tools images containing "L" data. JPEG
库能读取包含"L", "RGB", 或 "CMYK"模式数据的 JPEG, JFIF,和 Adobe
JPEG 文件，能够输出标准格式或者progressive 的JFIF 文件。
Using the draft method, you can speed things up by converting "RGB" images to
"L", and resize images to 1/2, 1/4 or 1/8 of their original size while loading them.
The draft method also configures the JPEG decoder to trade some quality for speed.
open 方法会设置以下info 属性：
jfif
• JFIF application marker found. If the file is not a JFIF file, this key is not
present.
adobe
• Adobe application marker found. If the file is not an Adobe JPEG file, this
key is not present.
progression
• Indicates that this is a progressive JPEG file.
The save method supports the following options:
quality
• The image quality, on a scale from 1 (worst) to 100 (best). The default is 75.
optimize
• If present, indicates that the encoder should make an extra pass over the
image in order to select optimal encoder settings.
progression
• If present, indicates that this image should be stored as a progressive JPEG
file.
Note: To enable JPEG support, you need to build and install the IJG JPEG library
before building the Python Imaging Library. See the distribution README for
details. MIC (只读)
The library identifies and reads Microsoft Image Composer (MIC) files. When
opened, the first sprite in the file is loaded. You can use seek and tell to read other
sprites from the file. MCIDAS (只读)
The library identifies and reads 8-bit McIdas area files. MPEG (只能识别)
The library identifies MPEG files. MSP
The library identifies and reads MSP files from Windows 1 and 2. The library
writes uncompressed (Windows 1) versions of this format. PCD (只读)
The library reads PhotoCD files containing "RGB" data. By default, the 768x512
resolution is read. You can use the draft method to read the lower resolution
versions instead, thus effectively resizing the image to 384x256 or 192x128. Higher
resolutions cannot be read by the Python Imaging Library. PCX
The library reads and writes PCX files containing "1", "L", "P", or "RGB"
data. PDF (只写)
The library can write PDF (Acrobat) images. Such images are written as binary
PDF 1.1 files, using either JPEG or HEX encoding depending on the image mode
(and whether JPEG support is available or not). PNG
The library identifies, reads, and writes PNG files containing "1", "L", "P",
"RGB", or "RGBA" data. Interlaced files are currently not supported.
open 方法会设置以下info 属性：
gamma
• Gamma 值，以浮点数的形式给出。
transparency
• 透明色索引。如果图像不是透明调色板图，则此键值被忽略。
save 方法支持以下选项：
optimize
• If present, instructs the PNG writer to make the output file as small as
possible. This includes extra processing in order to find optimal encoder
settings.
Note: To enable PNG support, you need to build and install the ZLIB compression
library before building the Python Imaging Library. See the distribution README
for details. PPM
库能够读写包含 "1", "L" 或 "RGB" 模式数据的 PBM, PGM 和 PPM 文
件。 PSD (只读)
The library identifies and reads PSD files written by Adobe Photoshop 2.5 and
3.0. SGI (只读)
The library reads uncompressed "L" and "RGB" files. This driver is highly
experimental. SUN (只读)
The library reads uncompressed "1", "P", "L" and "RGB" files. TGA (只读)
The library reads 24- and 32-bit uncompressed and run-length encoded TGA
files. TIFF
The library reads and writes TIFF files containing "1", "L", "RGB", or "CMYK"
data. It reads both striped and tiled images, pixel and plane interleaved multi-band
images, and either uncompressed, or Packbits, LZW, or JPEG compressed images.
In the current version, PIL always writes uncompressed TIFF files.
open 方法会设置以下info 属性：
compression
• 压缩模式。
In addition, the tag attribute contains a dictionary of decoded TIFF fields. Values
are stored as either strings or tuples. Note that only short, long and ASCII tags are
correctly unpacked by this release. XBM
库能够读写 X bitmap 文件 (模式"1")。 XPM (只读)
库能够读取256 色或者更少颜色的X pixmap 文件 (模式"P")。
open 方法会设置以下info 属性：
transparency
• 透明色索引。如果图像不是透明的，则此键值被忽略。
文件扩展名
Python Imaging Library 会把一些文件扩展名同特定的文件类型相关联。open
函数根据文件的内容来识别文件，而不是名字。但是save 方法会查看文件名来
决定使用哪种格式，除非显示的指定格式。类型扩展名 BMP ".bmp",
".dib" CUR ".cur" DCX ".dcx" EPS ".eps", ".ps" FLI ".fli", ".flc" FPX
".fpx" GBR ".gbr" GD ".gd" GIF ".gif" ICO ".ico" IM ".im" JPEG ".jpg",
".jpe", ".jpeg" MIC ".mic" MSP ".msp" PCD ".pcd" PCX ".pcx" PDF
".pdf" PNG ".png" PPM ".pbm", ".pgm", ".ppm" PSD ".psd" SGI ".bw", ".rgb",
".cmyk" SUN ".ras" TGA ".tga" TIFF ".tif", ".tiff" XBM ".xbm" XPM ".xpm"
要注意的是，PIL 库并不支持所有这些格式的保存操作。
编写自己的文件解码器
The Python Imaging Library uses a plug-in model which allows you to add your
own decoders to the library, without any changes to the library itself. Such plug-ins
have names like XxxImagePlugin.py, where Xxx is a unique format name (usually
an abbreviation).
A decoder plug-in should contain a decoder class, based on the ImageFile base
class defined in the module with the same name. This class should provide an
_open method, which reads the file header and sets up at least the mode and size
attributes. To be able to load the file, the method must also create a list of tile
descriptors. The class must be explicitly registered, via a call to the Image module.
For performance reasons, it is important that the _open method quickly rejects files
that do not have the appropriate contents. Example
The following plug-in supports a simple format, which has a 128-byte header
consisting of the words "SPAM" followed by the width, height, and pixel size in bits.
The header fields are separated by spaces. The image data follows directly after the
header, and can be either bi-level, greyscale, or 24-bit true
colour. File: SpamImagePlugin.py
切换行号显示
1 import Image, ImageFile
2 import string
3
4 class SpamImageFile(ImageFile.ImageFile):
5
6 format = "SPAM"
7 format_description = "Spam raster image"
8
9 def _open(self):
10
11 # check header
12 header = self.fp.read(128)
13 if header[:4] != "SPAM":
14 raise SyntaxError, "not a SPAM file"
15
16 header = string.split(header)
17
18 # size in pixels (width, height)
19 self.size = int(header[1]), int(header[2])
20
21 # mode setting
22 bits = int(header[3])
23 if bits == 1:
24 self.mode = "1"
25 elif bits == 8:
26 self.mode = "L"
27 elif bits == 24:
28 self.mode = "RGB"
29 else:
30 raise SyntaxError, "unknown number of bits"
31
32 # data descriptor
33 self.tile = [
34 ("raw", (0, 0) + self.size, 128, (self.mode, 0, 1))
35 ]
36
37 Image.register_open("SPAM", SpamImageFile)
38
39 Image.register_extension("SPAM", ".spam")
40 Image.register_extension("SPAM", ".spa") # dos version
41
The format handler must always set the size and mode attributes. If these are not set,
the file cannot be opened. To simplify the decoder, the calling code considers
exceptions like SyntaxError, KeyError, and IndexError, as a failure to identify the
file.
Note that the decoder must be explicitly registered using the register_open function
in the Image module. Although not required, it is also a good idea to register any
extensions used by this format. The Tile Attribute
To be able to read the file as well as just identifying it, the tile attribute must also be
set. This attribute consists of a list of tile descriptors, where each descriptor
specifies how data should be loaded to a given region in the image. In most cases,
only a single descriptor is used, covering the full image.
The tile descriptor is a 4-tuple with the following contents:
• (decoder, region, offset, parameters)
The fields are used as follows:
decoder
• Specifies which decoder to use. The "raw" decoder used here supports
uncompressed data, in a variety of pixel formats. For more information on
this decoder, see the description below.
region
• A 4-tuple specifying where to store data in the image.
offset
• Byte offset from the beginning of the file to image data.
parameters
• Parameters to the decoder. The contents of this field depends on the decoder
specified by the first field in the tile descriptor tuple. If the decoder doesn't
need any parameters, use None for this field.
Note that the tile attribute contains a list of tile descriptors, not just a single
descriptor. The Raw Decoder
The raw decoder is used to read uncompressed data from an image file. It can be
used with most uncompressed file formats, such as PPM, BMP, uncompressed
TIFF, and many others. To use the raw decoder with the fromstring function, use
the following syntax:
• image = fromstring(
o mode, size, data, "raw", raw mode, stride, orientation )
When used in a tile descriptor, the parameter field should look like:
• (raw mode, stride, orientation)
The fields are used as follows:
raw mode
• The pixel layout used in the file, and is used to properly convert data to
PIL's internal layout. For a summary of the available formats, see the table
below.
stride
• The distance in bytes between two consecutive lines in the image. If 0, the
image is assumed to be packed (no padding between lines). If omitted, the
stride defaults to 0.
orientation
• Whether the first line in the image is the top line on the screen (1), or the
bottom line (-1). If omitted, the orientation defaults to 1.
The raw mode field is used to determine how the data should be unpacked to match
PIL's internal pixel layout. PIL supports a large set of raw modes; for a complete
list, see the table in the Unpack.c module. The following table describes some
commonly used raw modes: mode description "1" 1-bit bilevel, stored with the
leftmost pixel in the most significant bit. 0 means black, 1 means white. "1;I" 1-bit
inverted bilevel, stored with the leftmost pixel in the most significant bit. 0 means
white, 1 means black. "1;R" 1-bit reversed bilevel, stored with the leftmost pixel in
the least significant bit. 0 means black, 1 means white. "L" 8-bit greyscale. 0 means
black, 255 means white. "L;I" 8-bit inverted greyscale. 0 means white, 255 means
black. "P" 8-bit palette-mapped image. "RGB" 24-bit true colour, stored as (red,
green, blue). "BGR" 24-bit true colour, stored as (blue, green, red). "RGBX" 24-bit
true colour, stored as (blue, green, red, pad). "RGB;L" 24-bit true colour, line
interleaved (first all red pixels, the all green pixels, finally all blue pixels).
Note that for the most common cases, the raw mode is simply the same as the mode.
The Python Imaging Library supports many other decoders, including JPEG, PNG,
and PackBits. For details, see the decode.c source file, and the standard plug-in
implementations provided with the library. Decoding Floating Point Data
PIL provides some special mechanisms to allow you to load a wide variety of
formats into a mode "F" (floating point) image memory.
You can use the "raw" decoder to read images where data is packed in any
standard machine data type, using one of the following raw modes: mode
description "F" 32-bit native floating point. "F;8" 8-bit unsigned integer. "F;8S"
8-bit signed integer. "F;16" 16-bit little endian unsigned integer. "F;16S" 16-bit
little endian signed integer. "F;16B" 16-bit big endian unsigned integer. "F;16BS"
16-bit big endian signed integer."F;16N" 16-bit native unsigned integer. "F;16NS"
16-bit native signed integer. "F;32" 32-bit little endian unsigned integer. "F;32S"
32-bit little endian signed integer. "F;32B" 32-bit big endian unsigned
integer."F;32BS" 32-bit big endian signed integer. "F;32N" 32-bit native unsigned
integer. "F;32NS" 32-bit native signed integer. "F;32F" 32-bit little endian
floating point. "F;32BF" 32-bit big endian floating point."F;32NF" 32-bit native
floating point. "F;64F" 64-bit little endian floating point. "F;64BF" 64-bit big
endian floating point. "F;64NF" 64-bit native floating point. The Bit Decoder
If the raw decoder cannot handle your format, PIL also provides a special "bit"
decoder that can be used to read various packed formats into a floating point image
memory.
To use the bit decoder with the fromstring function, use the following syntax:
• image = fromstring(
o mode, size, data, "bit", bits, pad, fill, sign, orientation )
When used in a tile descriptor, the parameter field should look like:
• (bits, pad, fill, sign, orientation)
The fields are used as follows:
bits
• Number of bits per pixel (2-32). No default.
pad
• Padding between lines, in bits. This is either 0 if there is no padding, or 8 if
lines are padded to full bytes. If omitted, the pad value defaults to 8.
fill
• Controls how data are added to, and stored from, the decoder bit buffer.
fill=0
• Add bytes to the msb end of the decoder buffer; store pixels from the msb
end.
fill=1
• Add bytes to the lsb end of the decoder buffer; store pixels from the msb end.
fill=2
• Add bytes to the msb end of the decoder buffer; store pixels from the lsb end.
fill=3
• Add bytes to the lsb end of the decoder buffer; store pixels from the lsb
end. If omitted, the fill order defaults to 0.
sign
• If non-zero, bit fields are sign extended. If zero or omitted, bit fields are
unsigned.
orientation
• Whether the first line in the image is the top line on the screen (1), or the
bottom line (-1). If omitted, the orientation defaults to 1.
译注：中英文术语对照表
• affine 仿射
• alpha 透明度
• band 通道
• class 类
• decoder 解码器
• dictionary 字典
• draft 草稿
• enhance 增强
• exception 异常
• filter 滤波器
• function 函数
• histogram 直方图
• image 图像
• import 导入
• iterate 迭代
• iterator 跌代子
• list 列表
• mask 掩模
• method 方法
• mode 模式
• object 对象
• operator 运算符
• palette 调色板
• pixel 像素
• raster 光栅
• rotate 旋转
• sequence 序列
• size 大小
• socket 套接字
• thumbnails 缩略图
• threshold 阈值
• tuple 元组
• zoom 缩放
PythonImageLibrary 中文手册 (2008-02-23 15:35:12 由localhost 编辑)