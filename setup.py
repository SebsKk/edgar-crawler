from setuptools import setup, find_packages

setup(
    name="edgar_crawler",
    version="0.1.0",
    author="SebsKk",
    author_email="your.email@example.com",
    description="A tool for downloading and processing SEC EDGAR filings",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/SebsKk/edgar-crawler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4==4.8.2",
        "click==7.0",
        "cssutils==1.0.2",
        "numpy==1.24.4",
        "lxml==4.9.1",
        "pandas==1.5.3",
        "requests==2.31.0",
        "tqdm==4.42.1",
        "pathos==0.2.9",
        "urllib3==1.26.7"
    ],
    entry_points={
        "console_scripts": [
            "edgar-crawler=edgar_crawler.main:main",
        ],
    },
)