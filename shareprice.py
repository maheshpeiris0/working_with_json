import json
class JsonRead():
    def __init__(self, json_file):
        self.json_file = json_file
    
    def read_json(self):
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print('File not found')
            return None
        except json.decoder.JSONDecodeError:
            print('Error in decoding json file')
            return None
            

if __name__ == '__main__':
    json_file_path = 'dataset/gainers.json'
    json_read = JsonRead(json_file_path)
    data = json_read.read_json()
    print(data)