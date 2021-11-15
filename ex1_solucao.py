import pandas as pd


train_data = pd.read_csv('ex1_train_data.csv', delimiter=';')


def mse(Y, Y_pred):
    result = 1/len(Y) * sum((Y - Y_pred) ** 2)

    return result

best_a = None
best_b = None
best_mse = None

for a in range(1, 100):
    for b in range(0, 100):
        Y_pred = train_data['x'] * a + b

        new_mse = mse(train_data['y'], Y_pred)
        
        if best_mse is None or new_mse < best_mse:
            best_mse = new_mse
            best_a = a
            best_b = b


print('best_mse = %.3f, best_a = %d, best_b = %d' % (best_mse, best_a, best_b))