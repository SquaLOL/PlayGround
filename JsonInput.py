import json

def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contains invalid JSON")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

a = 'data.json'
data = read_json_file(a)
if data is not None:
    print(data)
