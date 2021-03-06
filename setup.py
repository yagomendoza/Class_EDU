import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CheapCameraProject-pkg-eduard.almar.oliva",
    version="0.0.1",
    author="Eduard Almar",
    author_email="eduard.almar.oliva@hp.com",
    description="A small example package",
    long_description=file: README.md
    long_description_content_type="text/markdown",
    url="https://github.azc.ext.hp.com/Computer-Vision-BCN/CheapCameraProject/",
    project_urls={
        "Bug Tracker": "https://github.azc.ext.hp.com/Computer-Vision-BCN/CheapCameraProject/tree/Camera/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)