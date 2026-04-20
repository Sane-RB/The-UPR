from setuptools import setup, find_packages

setup(
    name='YourPackageName',  # Replace with the name of your package
    version='0.1.0',        # Initial version
    packages=find_packages(),
    author='Your Name',      # Replace with your name
    author_email='treborchard@icloud.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),  # Assuming you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/Sane-RB/The-UPR',  # Replace with the URL of your package
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if different
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here
    ],
)