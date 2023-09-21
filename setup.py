from setuptools import setup
setup(
    name='spelunking',
    version='1.0',
    author='Nicholas Sharp',
    python_requires='>=3.10',
    packages=['spelunking'],
    install_requires=[
        "numpy",
        "jax",
        "jaxlib",
        "polyscope",
        "imageio"
    ]
)
