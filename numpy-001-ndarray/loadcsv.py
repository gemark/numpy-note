class loadcsv:

    def load_from_file(self, path: str) -> list:
        fs = open(path, 'r', encoding='gbk')
        data = fs.readlines()
        fs.close()
        datas = []
        for v in data:
            datas.append(v.split(","))
        return datas