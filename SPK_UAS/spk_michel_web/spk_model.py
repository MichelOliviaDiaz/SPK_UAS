from settings import DEV_SCALE_nama_produk, DEV_SCALE_ram, DEV_SCALE_processor, DEV_SCALE_storage, DEV_SCALE_harga_per_unit, DEV_SCALE_ukuran_layar

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7
        self.raw_weight = {
            'nama_produk': 6,
            'harga_per_unit': 7,
            'processor': 7,
            'ram': 8,
            'ukuran_layar': 7,
            'storage': 9
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]]
                temp2 = {v: k for k, v in setWeight.items()}[item[1]]

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': laptop['id'],
            'nama_produk': DEV_SCALE_nama_produk[laptop['nama_produk']],
            'harga_per_unit': DEV_SCALE_harga_per_unit[laptop['harga_per_unit']],
            'processor': DEV_SCALE_processor[laptop['processor']],
            'ram': DEV_SCALE_ram[laptop['ram']],
            'ukuran_layar': DEV_SCALE_ukuran_layar[laptop['ukuran_layar']],
            'storage': DEV_SCALE_storage[laptop['storage']]
        } for laptop in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        nama_produk = [] # max
        ram = [] # max
        processor = [] # max
        storage = [] # max
        ukuran_layar = [] # max
        harga_per_unit = [] # min
        for data in self.data:
            nama_produk.append(data['nama_produk'])
            ram.append(data['ram'])
            processor.append(data['processor'])
            storage.append(data['storage'])
            ukuran_layar.append(data['ukuran_layar'])
            harga_per_unit.append(data['harga_per_unit'])

        max_nama_produk = max(nama_produk)
        max_ram = max(ram)
        max_processor = max(processor)
        max_storage = max(storage)
        max_ukuran_layar = max(ukuran_layar)
        min_harga_per_unit = min(harga_per_unit)

        return [
            {   'id': data['id'],
                'nama_produk': data['nama_produk']/max_nama_produk, # benefit
                'ram': data['ram']/max_ram, # benefit
                'processor': data['processor']/max_processor, # benefit
                'storage': data['storage']/max_storage, # benefit
                'ukuran_layar': data['ukuran_layar']/max_ukuran_layar, # benefit
                'harga_per_unit': min_harga_per_unit/data['harga_per_unit'] # cost
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['nama_produk'] ** weight['nama_produk'] *
        row['ram'] ** weight['ram'] *
        row['processor'] ** weight['processor'] *
        row['storage'] ** weight['storage'] *
        row['ukuran_layar'] ** (-weight['ukuran_layar']) *
        row['harga_per_unit'] ** weight['harga_per_unit']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))