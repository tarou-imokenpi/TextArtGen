# TextArtGen: Generate Images with Random Text

The **TextArtGen** is a Python library that allows you to create images containing random text. This library is useful for generating synthetic image datasets for various purposes, such as training machine learning models, testing image processing algorithms, or simply creating art. It provides flexibility in terms of text content, font styles, colors, and output formats.

[日本語](README_JP.md)
## Installation
It will be registered in pip in due course.

Currently you can download and use src\TextArtGen\TextArtGen.py.
<!-- You can install the TextArtGen library using pip:

```bash
pip install TextArtGen
``` -->

## Usage

Here's an example of how to use the TextArtGen library to create images with random text:

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

Generates a specified number of images with random text and saves them to the specified output directory.

## Example 
To get only numbers, not including alphabets
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

If you want to output only Japanese hiragana
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
If you want to output only hiragana and katakana in Japanese
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

- The library uses the PIL (Pillow) library for image manipulation. Make sure to have Pillow installed (`pip install Pillow`).
- The generated images will be saved in the specified output directory with the specified filename format and extension.



## License

This library is released under the [MIT License](LICENSE).
