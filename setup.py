#!/usr/bin/env python3
"""
GitHub PR Demo Project 安装配置
"""

from setuptools import setup, find_packages
import os

# 读取版本信息
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            return f.read().strip()
    return '1.0.0'

# 读取长描述
def get_long_description():
    readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# 读取依赖
def get_requirements():
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='github-pr-demo',
    version=get_version(),
    description='GitHub PR 工作流程演示项目',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Demo Team',
    author_email='demo@example.com',
    url='https://github.com/cc12345/github-pr-demo',
    project_urls={
        'Bug Reports': 'https://github.com/cc12345/github-pr-demo/issues',
        'Source': 'https://github.com/cc12345/github-pr-demo',
        'Documentation': 'https://github.com/cc12345/github-pr-demo/blob/main/docs/',
    },
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    python_requires='>=3.8',
    install_requires=get_requirements(),
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'flake8>=6.0.0',
            'black>=23.0.0',
            'mypy>=1.0.0',
            'bandit>=1.7.0',
            'safety>=2.0.0',
        ],
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
            'myst-parser>=0.18.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'calculator=calculator:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='github pr demo calculator education',
    license='MIT',
)