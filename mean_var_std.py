import numpy as np

def calculate(list):
if len(list)!=9:
        raise ValueError("La lista debe contener 9 digitos")

    matrix= np.array(input_list).reshape(3,3)
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    results = {}
    for name, func in operations.items():
        results[name] = [
            func(matrix, axis=0).tolist(),  
            func(matrix, axis=1).tolist(),  
            func(matrix).item()             
        ]




    return calculations
