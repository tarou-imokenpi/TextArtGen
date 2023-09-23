# TextArtGen: Generate Images with Random Text

**TextArtGen**は、ランダムなテキストを含む画像を作成できるPythonライブラリです。このライブラリは、機械学習モデルのトレーニング、画像処理アルゴリズムのテスト、あるいは単にアートの作成など、様々な目的で合成画像データセットを生成するのに便利です。テキストの内容、フォントスタイル、色、出力形式に関して柔軟性があります。

[English](README.md)
## Installation

そのうちpipに登録します。

現在はsrc\TextArtGen\TextArtGen.pyをダウンロードして使用してください。
<!-- TextArtGenライブラリはpipを使ってインストールできます：

```bash
pip install TextArtGen
``` -->

## Usage

TextArtGenライブラリを使って、ランダムなテキストを含む画像を作成する方法の例です：

```python
from TextArtGen import TextImageGenerator

generator = TextImageGenerator()

generator.generate_images(
    image_size=(512, 512),
    text_length=3,
    num_images=100,
    font_path=r"font/path",
    output_dir="data",
)

```


### `generate_images`

ランダムなテキストを含む画像を指定された数だけ生成し、指定された出力ディレクトリに保存する。

## Example 
アルファベットを含まない数字のみを取得する場合
```python
from TextArtGen import TextImageGenerator

generator = TextImageGenerator(include_alphabet=False, include_digits=True)

generator.generate_images(
    image_size=(512, 512),
    text_length=3,
    num_images=100,
    font_path=r"font/path",
    output_dir="data",
)

```

日本語のひらがなだけを出力したい場合
```python
from TextArtGen import TextImageGenerator

generator = TextImageGenerator(
    include_hiragana=True,
    include_alphabet=False,
)

generator.generate_images(
    image_size=(512, 512),
    text_length=3,
    num_images=100,
    font_path=r"font/path",
    output_dir="data",
)

```
日本語のひらがなとカタカナだけを出力したい場合
```python
from TextArtGen import TextImageGenerator

generator = TextImageGenerator(
    include_hiragana=True,
    include_katakana=True
    include_alphabet=False,
)

generator.generate_images(
    image_size=(512, 512),
    text_length=3,
    num_images=100,
    font_path=r"font/path",
    output_dir="data",
)


```

## Notes

- このライブラリは画像操作に PIL (Pillow) ライブラリを使用します。Pillowがインストールされていることを確認してください(`pip install Pillow`)。
- 生成された画像は指定された出力ディレクトリに指定されたファイル名形式と拡張子で保存されます。


## License

This library is released under the [MIT License](LICENSE).
