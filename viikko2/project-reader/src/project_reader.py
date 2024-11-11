from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        deserialized = toml.loads(content) # toml.loads takes in a string containing standard TOML-formatted data and returns a dictionary containing the parsed data.
        print(deserialized)

        poetry_data = deserialized['tool']['poetry']
        name = poetry_data['name']
        description = poetry_data['description']
        license = poetry_data["license"]
        authors = poetry_data['authors']
        dependencies = list(poetry_data['dependencies'].keys()) 
        dev_dependencies = list(poetry_data['group']['dev']['dependencies'].keys()) 

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
        # return Project(deserialized["title"], deserialized[], deserialized[], deserialized[])
        # def __init__(self, name, description, dependencies, dev_dependencies):
