from django.shortcuts import render
import random

# Create your views here.

def band_name(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        pet = request.POST.get('pet')
        band_name = f"{city} {pet}"
        return render(request, 'websiteHTML/band_name.html', {'band_name': band_name})
    return render(request, 'websiteHTML/band_name.html')

from django.shortcuts import render

def tip_calculator(request):
    if request.method == 'POST':
        errors = []
        tip_list = [10, 12, 15]
        
        # Validação do valor total da conta
        try:
            totalBill = float(request.POST.get('totalBill'))
            if totalBill <= 0:
                errors.append("The total bill must be a positive number.")
        except ValueError:
            errors.append("Please enter a valid number for the total bill.")
        
        # Validação do valor da gorjeta
        try:
            tip = int(request.POST.get('tip'))
            if tip not in tip_list:
                errors.append("Please choose a valid tip percentage: 10, 12, or 15.")
        except ValueError:
            errors.append("Please enter a valid number for the tip percentage.")
        
        # Validação do número de pessoas
        try:
            splitBill = int(request.POST.get('splitBill'))
            if splitBill <= 0:
                errors.append("The number of people must be greater than zero.")
        except ValueError:
            errors.append("Please enter a valid integer for the number of people.")
        
        # Se não houver erros, calcula o valor total por pessoa
        if not errors:
            totalPay = tip / 100 * totalBill + totalBill
            totalPayPer = round(totalPay / splitBill, 2)
            return render(request, 'websiteHTML/tip_calculator.html', {
                'totalPayPer': totalPayPer,
                'totalBill': totalBill,
                'tip': tip,
                'splitBill': splitBill
            })
        
        # Se houver erros, retorna os erros e mantém os valores já inseridos
        return render(request, 'websiteHTML/tip_calculator.html', {
            'errors': errors,
            'totalBill': request.POST.get('totalBill'),
            'tip': request.POST.get('tip'),
            'splitBill': request.POST.get('splitBill')
        })

    return render(request, 'websiteHTML/tip_calculator.html')


def even_odd(request):
    result = None
    if request.method == 'POST':
        try:
            number = int(request.POST.get('number'))
            if number % 2 == 0 :
                result = f"Your number {number} is even!"
            else:
                result = f"Your number {number} is odd!"
        except ValueError:
            result = "Please enter a valid character"
    return render(request, 'websiteHTML/even_odd.html', {'result': result})

def home(request):
    return render(request, 'websiteHTML/home.html')


def r_p_s(request):
    result = None
    player_hand = None
    npc_hand = None
    error_message = None
    if request.method == 'POST':
        try:
            possible_nums = [0, 1, 2]
            player_hand = int(request.POST.get('player_hand'))
            npc_hand = random.randint(0, 2)

            if player_hand not in possible_nums:
                raise ValueError("Número inválido")
            
            # Determine the result
            if player_hand != npc_hand:
                if (player_hand == 0 and npc_hand == 1) or \
                   (player_hand == 1 and npc_hand == 2) or \
                   (player_hand == 2 and npc_hand == 0):
                    result = "You lose!"
                else:
                    result = "You won!"
            else:
                result = "It's a Draw! Try again!"
        except ValueError:
            error_message = "Please enter a valid number and try again, it can be 0, 1 or 2."

    return render(request, 'websiteHTML/r_p_s.html', {
        'result': result,
        'player_hand': player_hand,
        'npc_hand': npc_hand,
        'error_message': error_message
    })