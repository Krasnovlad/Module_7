# %
team1_num = 5
print('В команде Мастера кода участников: %s' % team1_num)

team2_num = 6
print('Итого сегодня в командах участников: %s и %s!\n' % (team1_num, team2_num))

# format
score2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score2))

team1_time = 18015.2
print('Волшебники данных решили задачи за {} с!\n'.format(team1_time))

# f-strings
score1 = 40
print(f'Команды решили {score1} и {score2} задач.')

challenge_result = 'Волшебники данных'
print(f'Результат битвы: победа команды {challenge_result}!')

tasks_total = sum((score1, score2))
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')