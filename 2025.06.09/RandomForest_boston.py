from pandas import read_csv
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data = read_csv(path_dir / "boston_filter.csv")

target = data["MEDV"]
data = data.drop("MEDV", axis=1)


x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=1)

model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        bootstrap=True,
        n_jobs=-1,
        random_state=1
)

model.fit(x_train, y_train)
pred = model.predict(x_test)

mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = root_mean_squared_error(y_test, pred)  
r2 = r2_score(y_test, pred)

print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R2: {r2:.4f}")


# MAE: 2.1123
# MSE: 9.6692
# RMSE: 3.1095
# R2: 0.8171