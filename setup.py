from setuptools import setup, find_namespace_packages


setup(name='Chatbot_by_IE',
      version='0.1.10',
      description='Chatbot: Addressbook, NoteBook, Sort file',
      url='https://github.com/Sanyavas/chatbot-team-project.git',
      author='Oleksandr Vasylyna, Oleh Vakulchyk, Nataleia Orlovska, Anton Sokhnenko, Polina Dyka',
      author_email='vasilinaoleksanrd@gmail.com',
      license='MIT',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
      packages=find_namespace_packages(),
      install_requires=["prompt_toolkit", "rarfile", "prettytable"],
      entry_points={"console_scripts": [
            "chatbot=app.menu:main"]}
      )
