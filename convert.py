import requests

finish = False

while finish == False: 
    # Demander a l'utilisateur la  monnaie qu'il detient 
    currency_own = input('Quelle monnais detenez vous ? ')
    # Demander a l'utilisateur vers quelle monnaie il va convertire son argent 
    currency_looking = input('Vers quelle monnaie voulez vous faire la conversion ? ')

    # Appelle API pour recuperer le taux de cette monnaie 

    r = requests.get(f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2026.2.15/v1/currencies/{currency_own}.min.json')
    own = r.json()

   

    money_own = float(input(f"Combien d'{currency_own} detenez vous ? "))

    own = own[currency_own][currency_looking]
    total = money_own*own

    print(total)

    finish = str(input('Avez vous fini ? '))

    if finish == 'oui' or finish == 'Oui': 
        finish = True 
    else: finish =False
    
