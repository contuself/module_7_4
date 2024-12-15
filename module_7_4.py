# %
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': '5'})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': '5', 'team2_num': 6})
#format
print('Команда Волшебники данных решила задач {score_2}!'.format(score_2 = '42'))
print('Волшебники данных решили задачи за {team1_time}!'.format(team1_time = '18015.2'))
#f строка
score_1, score_2 = 40, 42
print(f'Команды решили {score_1} и {score_2}')
challenge_result = 'Мастера кода'
print(f'Результат биты: победа команды {challenge_result}!')
tasks_total, time_avg = 82, 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на каждую!')