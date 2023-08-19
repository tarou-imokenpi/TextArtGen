from PIL import Image, ImageDraw, ImageFont
import random
import string
import os

# from loguru import logger


class TextImageGenerator:
    """
    A class for generating images with randomly generated text.

    This class allows you to create images containing randomly generated text
    using different character sets and customize various properties such as
    image size, font style, colors, and output directory.

    Args:
        include_alphabet (bool): Include ASCII alphabet characters.
        include_digits (bool): Include numeric digits.
        include_hiragana (bool): Include Hiragana characters.
        include_katakana (bool): Include Katakana characters.
        include_kanji (bool): Include Kanji characters.

    Attributes:
        characters (str): A string containing the selected characters for text generation.

    Methods:
        __generate_characters: Generate a string containing selected character sets.
        __generate_random_text: Generate random text with the specified length.
        __binary_search_font_size: Perform binary search for the appropriate font size.
        __create_image: Create an image with specified text and styling.
        generate_images: Generate multiple images with random text and specified properties.
    -----------------------------------------------------------------------------------------
    lang JP \n
    ランダムに生成されたテキストを含む画像を生成するためのクラスです。

    このクラスは、異なる文字セットを使用してランダムに生成されたテキストを含む画像を作成し、\n
    画像のサイズ、フォントスタイル、色、出力ディレクトリなどのさまざまなプロパティをカスタマイズすることができます。

    Parameters:
        include_alphabet (bool): ASCIIアルファベット文字を含めるかどうか\n
        include_digits (bool): 数字を含めるかどうか。\n
        include_hiragana (bool): ひらがな文字を含めるかどうか。\n
        include_katakana (bool): カタカナ文字を含めるかどうか。\n
        include_kanji (bool): 漢字文字を含めるかどうか。\n

    Attributes:
        characters (str): テキスト生成に使用される選択された文字セットを含む文字列。

    Methods:
        __generate_characters: 選択された文字セットを含む文字列を生成します。\n
        __generate_random_text: 指定された長さのランダムなテキストを生成します。\n
        __binary_search_font_size: テキストの適切なフォントサイズを求めるためのバイナリサーチを実行します。\n
        __create_image: 指定されたテキストとスタイルで画像を作成します。\n
        generate_images: ランダムなテキストと指定されたプロパティを持つ複数の画像を生成します。\n
    -----------------------------------------------------------------------------------------
    lang CN \n
    一个用于生成随机文本图像的类。

    通过该类，您可以使用不同的字符集创建包含随机生成文本的图像\n
    并自定义各种属性，如\n
    图像大小、字体样式、颜色和输出目录\n

    Parameters:
        include_alphabet (bool)： 包含 ASCII 字母字符\n
        include_digits (bool)： 包含数字\n
        include_hiragana (bool)： 包含平假名字符\n
        include_katakana (bool): 包括片假名字符： 包含片假名字符\n
        include_kanji (bool)： 包括汉字字符\n

    Attributes:
        characters (str)： 包含用于生成文本的选定字符的字符串

    Methods:
        __generate_characters： 生成包含选定字符集的字符串\n
        __generate_random_text： 生成指定长度的随机文本\n
        __binary_search_font_size： 执行二进制搜索，查找合适的字体大小\n
        __create_image（创建图像 用指定的文本和样式创建图像\n
        generate_images（生成图像 用随机文本和指定属性生成多个图像\n
    """

    def __init__(
        self,
        include_alphabet=True,
        include_digits=False,
        include_hiragana=False,
        include_katakana=False,
        include_kanji=False,
    ):
        """
        Initialize a TextImageGenerator instance.

        Parameters:
            include_alphabet (bool): Include ASCII alphabet characters.
            include_digits (bool): Include numeric digits.
            include_hiragana (bool): Include Hiragana characters.
            include_katakana (bool): Include Katakana characters.
            include_kanji (bool): Include Kanji characters.
        """
        self.characters = self.__generate_characters(
            include_hiragana,
            include_katakana,
            include_kanji,
            include_alphabet,
            include_digits,
        )

    def __generate_characters(
        self,
        include_hiragana,
        include_katakana,
        include_kanji,
        include_alphabet,
        include_digits,
    ):
        characters = ""

        if include_alphabet:
            characters += string.ascii_letters

        if include_digits:
            characters += string.digits

        if include_hiragana:
            characters += "".join(chr(i) for i in range(0x3041, 0x3097))  # ひらがな

        if include_katakana:
            characters += "".join(chr(i) for i in range(0x30A1, 0x30F7))  # カタカナ

        if include_kanji:
            characters += "".join(chr(i) for i in range(0x4E00, 0x9FA6))  # 漢字

        return characters

    def __generate_random_text(self, length):
        return "".join(random.choice(self.characters) for _ in range(length))

    def __binary_search_font_size(self, text):
        lower_bound = 1
        upper_bound = 1000

        while lower_bound <= upper_bound:
            mid_font_size = (lower_bound + upper_bound) // 2
            temp_font = ImageFont.truetype(self.font_path, mid_font_size)
            text_width, text_height = temp_font.getsize(text)

            if (
                text_width < self.image_size[0] * 0.9
                and text_height < self.image_size[1] * 0.9
            ):
                lower_bound = mid_font_size + 1
            else:
                upper_bound = mid_font_size - 1

        return upper_bound

    def __create_image(
        self,
        text,
        color_mode=True,
        font_color=None,
        background_color=None,
    ):
        """
        Create an image with the specified text and styling.

        Parameters:
            text (str): Text to be displayed on the image.
            color_mode (bool): Whether to create the image in color mode.
            font_color (tuple or int): Font color (R, G, B) or grayscale value.
            background_color (tuple or int): Background color (R, G, B) or grayscale value.

        Returns:
            PIL.Image.Image: Generated image.
        """
        if color_mode:
            if font_color is None:
                font_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            if background_color is None:
                background_color = (255, 255, 255)
        else:
            if font_color is None:
                font_color = 0  # 文字色は黒
            if background_color is None:
                background_color = 255  # 背景色は白

        if color_mode:
            image = Image.new("RGB", self.image_size, background_color)
        else:
            image = Image.new("L", self.image_size, background_color)

        adjusted_font_size = self.__binary_search_font_size(text)
        font = ImageFont.truetype(self.font_path, adjusted_font_size)

        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(text, font=font)
        position = (
            (self.image_size[0] - text_width) // 2,
            (self.image_size[1] - text_height) // 2,
        )

        draw.text(position, text, font=font, fill=font_color)
        return image

    def generate_images(
        self,
        image_size,
        font_path,
        num_images=10,
        text_length=3,
        color_mode=True,
        output_dir="data",
        filename_mode="numbered",
        font_color=None,
        background_color=None,
        file_format="jpg",
    ):
        """
        Generate multiple images with random text and specified properties.

        Parameters:
            image_size (tuple): Size of the generated images (width, height).
            font_path (str): Path to the font file to be used.
            num_images (int): Number of images to generate.
            text_length (int): Length of the randomly generated text.
            color_mode (bool): Whether to generate images in color mode.
            output_dir (str): Directory to save the generated images.
            filename_mode (str): Filename mode ('numbered' or 'text').
            font_color (tuple or int): Font color (R, G, B) or grayscale value.
            background_color (tuple or int): Background color (R, G, B) or grayscale value.
            file_format (str): Format of the generated image files.

        Returns:
            None
        ------------------------------------------------------------------------------------
        lang JP\n
        指定されたプロパティで複数の画像を生成します。

        Parameters:
            image_size (tuple): 生成される画像のサイズ (幅, 高さ)。\n
            font_path (str): 使用されるフォントファイルへのパス。\n
            num_images (int): 生成する画像の数。\n
            text_length (int): ランダムに生成されるテキストの長さ。\n
            color_mode (bool): カラーモードで画像を生成するかどうか。\n
            output_dir (str): 生成された画像を保存するディレクトリ。\n
            filename_mode (str): ファイル名のモード（'numbered' または 'text'）。\n
            font_color (tuple or int): フォントの色 (R, G, B) またはグレースケール値。\n
            background_color (tuple or int): 背景色 (R, G, B) またはグレースケール値。\n
            file_format (str): 生成される画像ファイルのフォーマット。\n

        Returns:
            None
        -----------------------------------------------------------------------------------
        lang CN\n
        使用指定的属性生成多张图像
        Parameters:
            image_size (tuple): 生成的图像尺寸（宽度，高度）\n
            font_path (str): 要使用的字体文件的路径\n
            num_images (int): 要生成的图像数量\n
            text_length (int): 随机生成的文本长度\n
            color_mode (bool): 是否以彩色模式生成图像\n
            output_dir (str): 保存生成图像的目录\n
            filename_mode (str): 文件名模式（'numbered' 或 'text'）\n
            font_color (tuple 或 int): 字体颜色（R，G，B）或灰度值\n
            background_color (tuple 或 int): 背景颜色（R，G，B）或灰度值\n
            file_format (str): 生成的图像文件格式\n

        Returns:
            None
        """
        self.image_size = image_size
        self.font_path = font_path
        os.makedirs(output_dir, exist_ok=True)
        for i in range(num_images):
            random_text = self.__generate_random_text(text_length)
            generated_image = self.__create_image(
                random_text,
                color_mode,
                font_color=font_color,
                background_color=background_color,
            )
            if filename_mode == "numbered":
                image_path = os.path.join(output_dir, f"text_image_{i+1}.{file_format}")
            elif filename_mode == "text":
                filename = "".join(
                    c if c.isalnum() else "_" for c in random_text
                )  # ファイル名に使える文字だけ残す
                image_path = os.path.join(output_dir, f"{filename}.{file_format}")

            generated_image.save(image_path)

            # logger.debug(f"create img :{i+1} ")

            # if i == 0:
            #     generated_image.show()
