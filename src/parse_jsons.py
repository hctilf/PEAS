import json, os, re

class jsonAnalyzer:
    """some descr"""
    def __init__(self):
        self.json_files = []
        self.json_objs = {}
        self.cwd = os.getcwd()
        self.dict = ["epochs", "median(elapsed)", "median(instructions)", "median(cpucycles)", "median(branchinstructions)", "median(branchmisses)", "totalTime"]
    
    def gather_files(self):
        json_file_template = re.compile(r'^[.\w\d\s-]+([.]json){1}$')

        all_files = os.listdir()

        for file in all_files:
            if json_file_template.fullmatch(file):
                self.json_files.append(file)

    def load_jsons(self):
        for jfile in self.json_files:
            with open(jfile, 'r') as fp:
                self.json_objs[jfile.removesuffix(".json")] = json.load(fp)

    def get_result(self, json_name):
        print(json_name)
        for i in self.dict:
            print(i, self.json_objs[json_name]["results"][0][i])


if __name__ == "__main__":
    myData = jsonAnalyzer()

    myData.gather_files()
    print(myData.json_files)
    myData.load_jsons()
    # print(myData.json_objs)
    for i in myData.json_objs:
        myData.get_result(i)
        print("------------------------------------")
