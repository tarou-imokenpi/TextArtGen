from setuptools import setup, find_packages

try:
    with open("README.md") as f:
        readme = f.read()
except IOError:
    readme = ""


setup(
    name="TextArtGen",
    version="0.3.2",
    packages=find_packages(),
    install_requires=["Pillow"],
    description="Generates a random image from the specified font.\nJP:指定されたフォントからランダムに画像を生成します。",
    long_description=readme,
    license="MIT",
    author="shotaro",
    author_email="taro06360@gmail.com",
    maintainer="shotaro",
    maintainer_email="taro06360@gmail.com",
)
