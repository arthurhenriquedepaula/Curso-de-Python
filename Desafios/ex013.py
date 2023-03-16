wage = float(input('Digite o salário do funcionário: '))

new_wage = wage + wage * 15 / 100

print('O seu salário antigo era de: {:.2f} reais, e seu novo salário com o aumento é:{:.2f} reais' . format(wage, new_wage))