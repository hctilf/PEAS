import json, os, re

class jsonAnalyzer:
    """some descr"""
    def __init__(self):
        self.json_files = []
        self.json_objs = {}
        self.results = {}
        self.cwd = os.getcwd()
        self.dict = ["name", "epochs", "median(elapsed)", "median(instructions)", "median(cpucycles)", "median(branchinstructions)", "median(branchmisses)", "totalTime"]
        self.gather_files()
        self.load_jsons()
        for i in self.json_objs:
            self.form_results(i)

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

    def form_results(self, json_name):
        self.results[json_name] = {}
        for i in self.dict:
            self.results[json_name][i] = self.json_objs[json_name]["results"][0][i]
        self.form_add_results(json_name)

    def form_add_results(self, test):
        #form new data
        self.results[test]["ns/op"] = self.results[test]["median(elapsed)"] * 1e9
        self.results[test]["op/s"] = 1 / float(self.results[test]["median(elapsed)"])
        self.results[test]["ins/op"] = float(self.results[test]["median(instructions)"])
        self.results[test]["cyc/op"] = float(self.results[test]["median(cpucycles)"])
        self.results[test]["IPC"] = float(self.results[test]["median(instructions)"] / self.results[test]["median(cpucycles)"])
        self.results[test]["bra/op"] = float(self.results[test]["median(branchinstructions)"])
        #
        self.results[test]["median(elaps. ns.)"] = self.results[test]["median(elapsed)"] * 1e9
        self.results[test]["num_elem"] = int(self.results[test].pop('name'))

    def get_res(self) -> dict:
        return self.results

if __name__ == "__main__":

    myData = jsonAnalyzer()


    for i in myData.results:
        print("__________________________")
        print(i)
        print(myData.results[i])
        print("__________________________")
