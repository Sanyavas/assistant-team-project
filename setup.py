"""S E T U P"""

from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='Chatbot_by_IE',
      version='0.2.11',
      description='Chatbot: Addressbook, NoteBook, Sort file, Games',
      url='https://github.com/Sanyavas/chatbot-team-project.git',
      author='Oleksandr Vasylyna, Oleh Vakulchyk, Nataleia Orlovska, Anton Sokhnenko, Polina Dyka',
      author_email='vasilinaoleksanrd@gmail.com',
      license='MIT',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
      long_description=long_description,
      # data_files=[('app\\data', ['app\\data\\application.logs'])],
      # include_package_data=True,
      packages=find_namespace_packages(),
      install_requires=["prompt_toolkit", "rarfile", "prettytable", "rich"],
      entry_points={"console_scripts": [
            "chatbot=app.menu:main"]}
      )
