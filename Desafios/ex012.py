price = float(input('Digite o preço do produto: '))

new_price = price - price * 5 / 100 

print('O valor cheio é: {:.2f} já o valor promocional é: {:.2f}' .format(price, new_price))