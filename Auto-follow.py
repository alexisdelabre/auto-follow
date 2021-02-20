### Créer par Alexis Delabre
### Utilisation Python 3.8.6

import tweepy
import time

### TWITTER CREDENTIALS
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

### AUTH METHOD
def OAuth():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth
    except:
        return None

### AUTH CALL
oauth = OAuth()
API = tweepy.API(oauth)

### SCRIPT
my_sn = API.me().screen_name  # mon arobase
def Followings_manage():

    ## Choix de méthode, follow ou unfollow
    print('\nAuto-follow (1) ou Auto-unfollow (2)')
    methode = 0
    while True:
        methode = input('Entre ton choix (1 ou 2) : ')

        # Follow methode
        if methode == '1':
            def manage_friendship(user_id, index, lenght):
                API.create_friendship(user_id)
                user = API.get_user(id=user_id)
                print(f"@{user.screen_name} follow! Avancement: {index+1}/{lenght}")
            break

        # Unfollow methode
        elif methode == '2':
            def manage_friendship(user_id, index, lenght):
                API.destroy_friendship(user_id)
                user = API.get_user(id=user_id)
                print(
                    f"@{user.screen_name} unfollow! Avancement: {index+1}/{lenght}")
            break
        else:
            print('Uniquement 1 ou 2. Veuillez rééssayer\n')

    ## Methode choisie
    if methode == '1':
        print('\nAUTO FOLLOW SCRIPT\n')
    elif methode == '2':
        print('\nAUTO UNFOLLOW SCRIPT\n')

    ## Mon nombre d'abonnements
    my_followings_len_start = len(API.friends_ids(id=my_sn))
    print(f"Votre nombre actuel d'abonnements  : {my_followings_len_start}")

    ## Récupération des abonnements du compte ciblé, comptes IDs dans une liste
    while True:
        try:
            # récupération de l'arobase
            while True:
                user_sn = input('[?] Arobase du compte ciblé : @')
                validation = input(
                    f"[?] Récupération des abonnements de @{user_sn}, appuyez sur Entrer pour valider votre saisie.")
                if validation == '':
                    break
            followings_ids = API.friends_ids(screen_name=user_sn)
            print(
                f'[+] Récupération des abonnements de @{user_sn} effectuée!\n')
            break
        except:
            print("Erreur de saisie, veuillez vérifier l'arobase du compte ciblé.\n")
    time.sleep(1)

    ## Itération dans la liste des abonnements, puis follow
    lenght = len(followings_ids)
    for i in range(lenght):
        manage_friendship(followings_ids[i], i, lenght)
        time.sleep(5)  # Pause essentielle pour éviter le 'rate limit' de l'API

    ## Mon nombre d'abbonnements (update) & delta abonnements
    my_followings_len_end = len(API.friends_ids(id=my_sn))
    delta = my_followings_len_end-my_followings_len_start
    print(f"\n\nVotre nombre actuel d'abonnements : {my_followings_len_end}\n")
    print(f'[+] Différence abonnements : {delta}')


Followings_manage()
