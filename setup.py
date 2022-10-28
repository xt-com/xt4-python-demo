# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark: 
"""
import pathlib
import re

from setuptools import (setup, find_packages)


root_dir = pathlib.Path(__file__).parent
long_description = (root_dir / 'README.md').read_text(encoding='utf-8')

# PyPI disables the "raw" directive.
long_description = re.sub(
    r"^\.\. raw:: html.*?^(?=\w)",
    "",
    long_description,
    flags=re.DOTALL | re.MULTILINE,
)

REQUIRES = [
    "websocket-client",
]

setup(
    name="XTApiSDK",
    long_description=long_description,
    author='Lao Wang',
    version="0.0.2",
    license='BSD',
    author_email='1125564921@qq.com',
    url='https://xt-com.github.io/xt4-api/#balance_cnbalanceGet',
    packages=find_packages(),
    python_requires='>=3.7',
    setup_requires=REQUIRES,
    install_requires=REQUIRES,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    zip_safe=False,
)
