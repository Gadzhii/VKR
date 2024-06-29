import json

class CustomObject:
    def __init__(self, name):
        self.name = name

def serialize_data(obj):
    return json.dumps(obj.__dict__)

def deserialize_data(data):
    try:
        data_dict = json.loads(data)
        return CustomObject(**data_dict)
    except Exception as e:
        print(f"Ошибка десериализации: {e}")
        return None

if __name__ == "__main__":
    # Безопасная сериализация и десериализация
    safe_obj = CustomObject("Безопасный")
    serialized_safe = serialize_data(safe_obj)
    deserialized_safe = deserialize_data(serialized_safe)
    print(f"Десериализованный безопасный объект: {deserialized_safe.name}")

    # Пример ложного срабатывания
    def potentially_malicious_function(data):
        # Здесь идет просто проверка строки, но некоторые SAST анализаторы могут 
        # воспринять это как потенциально небезопасное действие
        if "malicious" in data:
            print("Найден потенциально опасный контент!")
        return "Безопасно"

    test_data = '{"name": "legit data"}'
    result = potentially_malicious_function(test_data)
    print(result)
