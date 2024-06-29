import pickle

# Имитация получения сериализованных данных из ненадежного источника
untrusted_data = b"cos\nsystem\n(S'echo Hello World'\ntR."

def unsafe_deserialization(data):
    # Десериализация данных без какой-либо валидации
    deserialized_object = pickle.loads(data)
    return deserialized_object

# Небезопасная десериализация
result = unsafe_deserialization(untrusted_data)
print(result)
