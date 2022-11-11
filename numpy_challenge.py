import numpy as np

if __name__ == "__main__":
  MrFirst = np.empty((5,6))
  MrsSecond = np.arange(24).reshape(2,3,4)
  MsThird = np.random.random((2,3))

#просто матричное перемножение через dot
def matrix_multiplication(mat1, mat2):
  mat3 = mat1.dot(mat2)

#на вход принимается список, каждый его элемент конвертирую в матрицу, сравниваю число колонок первой матрицы с числом строк последующей 
def multiplication_check(list1):
  for i in range(len(list1)-1):
    x = np.array(list1[i])
    y = np.array(list1[i+1])
    if x.shape[1] == y.shape[0]:
      return True
    else:
      return False

#прогоняю список с матрицами через предыдущую функцию, чтобы понять, а можно ли вообще их перемножать
#если можно, идет перемножение через multi_dot
def multiply_matrices(list2):
  if multiplication_check(list2):
    return np.linalg.multi_dot(list2)
  else:
    return None

#вычисляю Евклидово расстояние c помощью linalg.norm
def compute_2d_distance(point_1, point_2):
  dist = np.linalg.norm(point_1-point_2)
  print(dist)

#то же самое, только теперь на вход подаются одномерные эрреи с любым количеством значений 
#пользуюсь более громоздким методом, но он тоже рабочий
def compute_multidimensional_distance(point_1, point_2):
  distance = np.sqrt(sum(pow(point_1-point_2, 2)))
  print(distance)

#функция для рассчета матрицы попарных расстояний  
def compute_pair_distances(arr):
  pairdist = np.linalg.norm(arr[:, None, :] - arr, axis=-1)
  print(pairdist)