from setuptools import setup
setup(
    name='spelunking',
    version='1.0',
    author='Nicholas Sharp',
    python_requires='>=3.10',
    packages=['spelunking'],
    install_requires=[
        "numpy",
        "jax==0.4.9",
        "jaxlib==0.4.9",
        "polyscope",
        "imageio"
    ]
)
